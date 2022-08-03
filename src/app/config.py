import os

from dotenv import load_dotenv


load_dotenv(override=True)

class Config:
    APP_NAME    = os.getenv("APP_NAME")
    ENVIRONMENT = os.getenv("ENVIRONMENT")