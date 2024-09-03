import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    SQLALCHEMY_DATABASE_URI = os.environ["SQLALCHEMY_DATABASE_URI"]
    CELERY_NAME = os.environ["CELERY_NAME"]
    CELERY_BROKER = os.environ["CELERY_BROKER"]
    CELERY_EXCHANGE = os.environ["CELERY_EXCHANGE"]
    CELERY_EXCHANGE_TYPE = os.environ["CELERY_EXCHANGE_TYPE"]
    CELERY_BIND_KEY = os.environ["CELERY_BIND_KEY"]
    CELERY_BACKEND = os.environ["CELERY_BACKEND"]
