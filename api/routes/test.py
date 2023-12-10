from fastapi import APIRouter
from transformers import pipeline

router = APIRouter(tags=["generate"])

@router.get("/")
def test():

    return {'hello':'world'}


classifier = pipeline("text-classification")

@router.post("/classify")
def classify_text(text: str):
    # Use the Hugging Face model to classify the text
    result = classifier(text)

    # Return the classification result
    return {"classification": result[0]["label"], "confidence": result[0]["score"]}

# 
@router.post("/")
def test():

    return {'result':'res'}