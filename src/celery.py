from celery import Celery, Task
from flask import Flask
from src.config import Config

def celery_init_app(app: Flask) -> Celery:
    class FlaskTask(Task):
        def __call__(self, *args: object, **kwargs: object) -> object:
            with app.app_context():
                return self.run(*args, **kwargs)
    

    celery_app = Celery(
        app.name,
        task_cls=FlaskTask,
        backend=Config.CELERY_BACKEND,
        broker=Config.CELERY_BROKER
    )

    celery_app.conf.update(
        task_serializer="json",
        result_serializer="json",
        accept_content=["json"],
        worker_hijack_root_logger=True,
        worker_cancel_long_running_tasks_on_connection_loss=True,
        task_acks_late=True,
        task_queues={
            "webhook_event_worker": {
                "exchange": Config.CELERY_EXCHANGE,
                "exchange_type": Config.CELERY_EXCHANGE_TYPE,
                "binding_key": Config.CELERY_BIND_KEY,
            }
        },
    )

    app.extensions["celery"] = celery_app
    return celery_app