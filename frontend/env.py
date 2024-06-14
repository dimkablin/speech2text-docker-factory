import os
from dotenv import load_dotenv

load_dotenv()

# importing environment variables from .env file
BACKEND_URL = os.getenv("BACKEND_URL", default="http://127.0.0.1:8001")
VERIFY = os.getenv("VERIFY", default=False)