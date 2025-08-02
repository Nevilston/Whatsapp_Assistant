import os
from dotenv import load_dotenv

load_dotenv()
class Config:
    SQLALCHEMY_DATABASE_URI = os.getenv("SQLALCHEMY_DATABASE_URI")
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
    TWILIO_AUTH_TOKEN = os.getenv("TWILIO_AUTH_TOKEN")
