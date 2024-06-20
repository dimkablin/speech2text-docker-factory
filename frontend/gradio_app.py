from fastapi import HTTPException, UploadFile
import gradio as gr
import requests
import soundfile as sf
from io import BytesIO
from env import BACKEND_URL, VERIFY


def get_models():
    response = requests.get(f"{BACKEND_URL}/models", verify=VERIFY)
    if response.status_code == 200:
        return response.json()["models"]
    else:
        return ['Нет доступных моделей.']


def speech_to_text(audio, model_name):
    sr, samples = audio
    # Convert from numpy to bytes in PCM_16 WAV format
    bytes_io = BytesIO()
    sf.write(bytes_io, samples, sr, subtype='PCM_16', format='WAV')
    bytes_io.seek(0)

    files = {"audio_file": ("audio.wav", bytes_io, "audio/wav")}
    headers = {'accept': 'application/json'}
    
    response = requests.post(f"{BACKEND_URL}/predict?model_name={model_name}", 
                             files=files,
                             headers=headers,
                             verify=VERIFY)
    
    if response.status_code == 200:
        return response.json().get("transcription", "Error in transcription")
    else:
        return f"Error: {response.status_code} - {response.text}"


def update_model_config(model_name):
    response = requests.get(f"{BACKEND_URL}/get-config?model_name={model_name}",
                            verify=VERIFY)
    return response.json() if response.status_code == 200 else {}


def refresh_models_and_config():
    models = get_models()
    if models:
        config = update_model_config(models[0])
    else:
        config = {}
    return models, models[0] if models else "", config


def input2output(model_name, audio):
    # speech2text output
    s2t = speech_to_text(audio, model_name)

    # model config output
    model_config = update_model_config(model_name)

    return model_config, s2t


input_audio = gr.Audio(
    sources=["upload", "microphone"],
    waveform_options=gr.WaveformOptions(
        waveform_color="#00B473",
        waveform_progress_color="#00B473",
        skip_length=2,
        show_controls=False,
    ),
    interactive=True,
    show_download_button=True
)


# Интерфейс Gradio
with gr.Blocks() as iface:
    gr.Markdown(
        """
        # Модель распознования речи
        """
    )

    available_models, selected_model, model_config_value = refresh_models_and_config()

    # Выпадающее меню для выбора модели
    model_selector = gr.Dropdown(
        choices=available_models,
        label="Выбрать модель",
        value=selected_model
    )

    # Компонент для отображения конфигурации модели
    model_config = gr.JSON(
        label="Настройки модели",
        value=model_config_value)

    # Обновление конфигурации модели при изменении выбора модели
    model_selector.change(fn=update_model_config, 
                          inputs=model_selector, 
                          outputs=model_config)
    
    # Интерфейс для обработки аудио и отображения результата
    gr.Interface(
        fn=input2output,
        inputs=[model_selector, input_audio],
        outputs=[model_config, 
                 gr.Textbox(label="Распознанный текст.")],
        allow_flagging="never"
    )

    iface.load(fn=refresh_models_and_config,
               inputs=None,
               outputs=[model_selector, model_selector, model_config])
