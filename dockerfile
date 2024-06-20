# backend dockerfile 
# i need it to be here to move docker-compose.ynl file to the container

FROM python:3.10-slim

WORKDIR /app

COPY backend/requirements.txt .
COPY docker-compose.yml .

RUN apt-get update && apt-get install -y build-essential ffmpeg &&\
    pip install --no-cache-dir -r requirements.txt

COPY backend/ .

CMD ["uvicorn", "api.main:app", "--host", "0.0.0.0", "--port", "8000", "--reload", "--ssl-keyfile", "ssl/local_key.pem", "--ssl-certfile", "ssl/local_cert.pem"]
