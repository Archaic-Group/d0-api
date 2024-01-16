from fastapi import APIRouter

router = APIRouter(tags=["generate"])

@router.get("/")
def test():

    return {'hello':'world'}

@router.post("/classify")
def classify_text(text: str):
    return {'hello':'world'}

# 
@router.post("/")
def test():

    return {'result':'res'}