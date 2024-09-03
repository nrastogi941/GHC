import atexit
from flask import Flask
from src.databases import db
from src.resources.api import webhook
from src.config import Config
from src.schedular import scheduler
from src.celery import celery_init_app


app = Flask(__name__)

# load the configs
app.config.from_object(Config)

# init db
db.init_app(app)

#start schedular
scheduler.start()

# Initialize Celery with the Flask app
celery_app = celery_init_app(app)


# Register Blueprints
app.register_blueprint(webhook)


@app.route("/", methods=["GET", "POST"])
def check():
    return "Up and Running..."


# Shut down the scheduler when exiting the app
atexit.register(scheduler.shutdown)
if __name__ == '__main__':
    app.run(debug=True)




































# import atexit
# from flask import Flask
# from src.databases import db
# from src.resources.api import webhook
# from src.config import Config
# from src.celery import make_celery
# from apscheduler.schedulers.background import BackgroundScheduler
# from apscheduler.jobstores.sqlalchemy import SQLAlchemyJobStore


# app = Flask(__name__)

# # load the configs
# app.config.from_object(Config)

# # init db
# db.init_app(app)

# # Initialize Celery with the Flask app
# celery = make_celery(app)

# # Register Blueprints
# app.register_blueprint(webhook)


# # APScheduler configuration
# scheduler = BackgroundScheduler()
# scheduler.add_jobstore(SQLAlchemyJobStore(url='mysql://root:password123@localhost/dhc'))
# scheduler.start()



# @app.route("/", methods=["GET", "POST"])
# def check():
#     return "Up and Running..."


# def schedule_job(**kwargs):
#     try:
#         print(kwargs)
#         task_time = kwargs.get("task_time")
#         print(task_time)
#         scheduler.add_job(
#             send_task_to_celery, 
#             'date', 
#             run_date=task_time,
#             kwargs=kwargs
#         )
#         jobs = scheduler.get_jobs()
#         print("Currently scheduled jobs:", jobs)
#         db.session.commit()
#         print("Job scheduled successfully.")
#     except Exception as e:
#         print(f"Error: schedule_job: {e}")


# def send_task_to_celery(**kwargs):

#     task_id = kwargs.get("task_id")
#     print(kwargs)

#     # celery_app.send_task(
#     #     "send_scheduled_messages",
#     #     task_id=task_id,
#     #     kwargs=kwargs,
#     #     exchange=Config.CELERY_EXCHANGE,
#     #     routing_key=Config.CELERY_BIND_KEY
#     # )


# # Shut down the scheduler when exiting the app
# # atexit.register(scheduler.shutdown)

# if __name__ == '__main__':
#     app.run(debug=True)


