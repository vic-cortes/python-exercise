import os

from dotenv import load_dotenv


load_dotenv(override=True)

class Config:
    DUMMY_VARIABLE = os.getenv("DUMMY_VARIABLE")