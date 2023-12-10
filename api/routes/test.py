import logging
from typing import List, Union

from fastapi import APIRouter, HTTPException
from PIL import Image

router = APIRouter(tags=["generate"])


@router.post("/txt2img")
def test(test):
    "Generate images from text"

    try:
        images: Union[List[Image.Image], List[str]]
        time: float
        # images, time = gpu.generate(test)
    # except ModelNotLoadedError:
    except:
        raise HTTPException(status_code=400, detail="Model is not loaded")

    return (images, time)