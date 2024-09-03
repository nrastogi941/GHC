from src.resources.model import Checkout
from src.app import celery_app
from flask import current_app as app
from src.databases import db


@celery_app.task(acks_late=True, bind=True, name="send_scheduled_messages")
def send_scheduled_messages(self, *args, **kwargs):
    print(kwargs)
    checkout_id = kwargs.get("checkout_id")
    checkout = Checkout.query.get(checkout_id)
    if not checkout or checkout.order_placed:
        return

    messages = [
        "Reminder: Complete your purchase!",
        "Still interested?", 
        "Last chance to get your items!"
    ]
    if checkout.messages_sent < len(messages):
        send_message(checkout.user_email, messages[checkout.messages_sent])
        checkout.messages_sent += 1
        db.session.commit()


def send_message(user_email, message):
    print(f"Sending message to {user_email}: {message}")