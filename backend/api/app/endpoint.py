from fastapi import APIRouter, HTTPException, UploadFile, File
import requests
from utils.model_manager import get_running_models

router = APIRouter()


@router.get("/models")
async def list_models():
    """ Rutern all available containers. """
    models = get_running_models()
    if not models:
        raise HTTPException(status_code=404, detail="No models found")
    return {"models": models}


@router.post("/predict")
async def predict(model_name: str, audio_file: UploadFile = File(...)):
    """ Use container with name model_name to predict. """
    models = get_running_models()
    if model_name not in models:
        raise HTTPException(status_code=404, detail="Model not found")
    
    files = {"file": (audio_file.filename, audio_file.file, audio_file.content_type)}
    response = requests.post(f"http://{model_name}:8000/predict", files=files)
    
    if response.status_code != 200:
        raise HTTPException(status_code=response.status_code, detail=response.text)
    
    return response.json()


@router.get("/get-config")
async def get_config(model_name: str):
    """ Return model config. """
    models = get_running_models()
    if model_name not in models:
        raise HTTPException(status_code=404, detail="Model not found")
    
    response = requests.get(f"http://{model_name}:8000/get-config")
    
    if response.status_code != 200:
        raise HTTPException(status_code=response.status_code, detail=response.text)
    
    return response.json()
