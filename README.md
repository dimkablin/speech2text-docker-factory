# Speech2Text Project

## Описание

Этот проект предоставляет функционал для преобразования речи в текст с использованием различных моделей, развернутых в Docker-контейнерах. Проект состоит из Backend (FastAPI) и Frontend (Gradio).

## Структура проекта

```
├── backend
│   ├── api
│   │   ├── app
│   │   │   ├── endpoint.py         # Основные эндпоинты FastAPI
│   │   │   └── middleware.py       # Middleware для обработки запросов и ответов
│   │   └── main.py                 # Основной файл для запуска FastAPI приложения
│   ├── dockerfile                  # Dockerfile для сборки образа backend-сервиса
│   ├── env.py                      # Конфигурационные параметры и переменные окружения для backend
│   ├── main.py                     # Точка входа для запуска backend приложения
│   ├── ssl
│   │   ├── local_cert.pem          # Локальный SSL-сертификат для защищённых соединений
│   │   └── local_key.pem           # Локальный SSL-ключ для защищённых соединений
│   └── utils
│       └── model_manager.py        # Утилиты для управления моделями и их загрузкой
│      
├── frontend
│   ├── env.py                      # Конфигурационные параметры и переменные окружения для frontend
│   ├── gradio_app.py               # Gradio приложение для интерфейса пользовательских взаимодействий
│   ├── main.py                     # Точка входа для запуска frontend приложения
│   └── ssl
│       ├── local_cert.pem          # Локальный SSL-сертификат для защищённых соединений
│       └── local_key.pem           # Локальный SSL-ключ для защищённых соединений
│   
├── LICENSE                         # Лицензионное соглашение проекта
├── docker-compose.yml              # Docker Compose файл для оркестрации контейнеров backend и frontend
├── README.md                       # Документация и инструкции по проекту
└── requirements.txt                # Зависимости Python для установки через pip

```

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
