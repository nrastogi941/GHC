from apscheduler.schedulers.background import BackgroundScheduler
from apscheduler.jobstores.sqlalchemy import SQLAlchemyJobStore
from src.config import Config

# APScheduler configuration
scheduler = BackgroundScheduler()
scheduler.add_jobstore(SQLAlchemyJobStore(url=Config.SQLALCHEMY_DATABASE_URI))
