import logging
from pathlib import Path

from fastapi import FastAPI, Depends, Request, status
from fastapi.exceptions import RequestValidationError
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse, FileResponse
from fastapi.staticfiles import StaticFiles
from routes import test,root


logger = logging.getLogger(__name__)

async def log_request(request: Request):
    logger.debug(f"url: {request.url}")

# Main
app = FastAPI(
    docs_url="/api/docs",
    redoc_url="/api/redoc",
    dependencies=[Depends(log_request)]
)

# Routes
app.include_router(root.router, prefix="", tags=["root"])
app.include_router(test.router, prefix="/test", tags=["test"])


# Exception handlers
@app.exception_handler(RequestValidationError)
async def validation_exception_handler(request: Request, exc: RequestValidationError):
    content = {
        "status_code": 422,
        "message": str(exc),
        "data": None,
    }
    return JSONResponse(content=content, status_code=status.HTTP_422_UNPROCESSABLE_ENTITY)

# Startup and shutdown events
@app.on_event("startup")
async def startup_event():
    logger.info("Started application")

@app.on_event("shutdown")
async def shutdown_event():
    logger.info("Shutting down application")


# CORS configuration
origins = ["*"]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
