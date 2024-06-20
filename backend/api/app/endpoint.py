from fastapi import APIRouter, HTTPException, UploadFile, File
import requests
from utils.model_manager import get_speech2text_urls

router = APIRouter()


@router.get("/models")
async def list_models():
    """ Rutern all available containers. """
    urls = get_speech2text_urls()
    models = list(urls.keys())
    if not models:
        raise HTTPException(status_code=404, detail="No models found")
    return {"models": models}


@router.post("/predict")
async def predict(model_name: str, audio_file: UploadFile = File(...)):
    """ Use container with name model_name to predict. """
    urls = get_speech2text_urls()
    models = list(urls.keys())

    if model_name not in models:
        raise HTTPException(status_code=404, detail="Model not found")
    
    files = {"audio_file": (audio_file.filename, audio_file.file, audio_file.content_type)}
    response = requests.post(f"https://{model_name}:{urls[model_name]}/predict", 
                             files=files, 
                             verify=False)
    
    if response.status_code != 200:
        raise HTTPException(status_code=response.status_code, detail=response.text)
    
    return response.json()


@router.get("/get-config")
async def get_config(model_name: str):
    """ Return model config. """
    urls = get_speech2text_urls()
    models = list(urls.keys())

    if model_name not in models:
        raise HTTPException(status_code=404, detail="Model not found")
    
    response = requests.get(f"https://{model_name}:{urls[model_name]}/get-config", 
                            verify=False)
    
    if response.status_code != 200:
        raise HTTPException(status_code=response.status_code, detail=response.text)
    
    return response.json()
