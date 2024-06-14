# Speech2Text Project

## Описание

Этот проект предоставляет функционал для преобразования речи в текст с использованием различных моделей, развернутых в Docker-контейнерах. Проект состоит из Backend (FastAPI) и Frontend (Gradio).

## Структура проекта

- `backend/` - Содержит код и настройки для Backend.
- `frontend/` - Содержит код и настройки для Frontend.
- `docker-compose.yml` - Конфигурация Docker Compose для развертывания проекта.
- `README.md` - Описание проекта.

## Запуск проекта

1. Склонируйте репозиторий:
    ```bash
    git clone <your-repo-url>
    cd speech2text_project
    ```

2. Запустите Docker Compose:
    ```bash
    docker-compose up --build
    ```

3. Откройте браузер и перейдите на `http://localhost:7860`, чтобы использовать интерфейс Gradio.
