import os
from dotenv import load_dotenv


load_dotenv()

MODEL = os.getenv("GEMINI_MODEL", "gemini-1")
API_KEY = os.getenv("GEMINI_API_KEY")

if not API_KEY:
    raise ValueError("GEMINI_API_KEY not set in environment variables")
