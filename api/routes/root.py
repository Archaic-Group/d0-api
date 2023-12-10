from fastapi import APIRouter

router = APIRouter(tags=["root"])

@router.get("/")
def test():

    return {'hello':'world'}