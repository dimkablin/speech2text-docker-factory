import os
from dotenv import load_dotenv

load_dotenv()

# importing environment variables from .env file
BACKEND_URL = os.getenv("BACKEND_URL", default="https://127.0.0.1:8001")