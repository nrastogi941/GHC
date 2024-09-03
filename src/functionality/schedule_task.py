from src.config import Config
from src.schedular import scheduler


def schedule_job(**kwargs):
    try:
        print(kwargs)
        task_time = kwargs.get("task_time")
        print(task_time)
        scheduler.add_job(
            send_task_to_celery, 
            'date', 
            run_date=task_time,
            kwargs=kwargs
        )
        print("Job scheduled successfully.")
    except Exception as e:
        print(f"Error: schedule_job: {e}")


def send_task_to_celery(**kwargs):
    from src.app import celery_app

    task_id = kwargs.get("task_id")
    print(kwargs)

    celery_app.send_task(
        "send_scheduled_messages",
        task_id=task_id,
        kwargs=kwargs,
        exchange=Config.CELERY_EXCHANGE,
        routing_key=Config.CELERY_BIND_KEY
    )