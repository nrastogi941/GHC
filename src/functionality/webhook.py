import datetime
import uuid
from src.databases import db
from src.resources.model import Checkout
from src.functionality.schedule_task import schedule_job

def checkout_abandoned_handler(event_payload):
    user_email = event_payload.get('email')
    checkout_time = datetime.datetime.now()
    checkout = Checkout(
        user_email=user_email, 
        checkout_time=checkout_time
    )
    db.session.add(checkout)
    db.session.commit()

    if checkout:
        time_intervals = [
            datetime.timedelta(minutes=1), 
            datetime.timedelta(days=1), 
            datetime.timedelta(days=2)
        ]
        for interval in time_intervals:
            kwargs = {
                'task_time': checkout_time + interval,
                'task_id': str(uuid.uuid4()),
                'checkout_id': checkout.id
            }
            schedule_job(**kwargs)

    return {"message": "Checkout abandonment recorded"}, 200


def order_placed_handler(event_payload):
    order = event_payload.get('order')
    user_email = order.get('email')
    print(user_email)

    checkout = Checkout.query.filter_by(user_email=user_email).first()
    if checkout:
        ordered_items = [
            {
                "name": item['name'],
                "quantity": item['quantity'],
                "id": item['id']
            } 
            for item in order['line_items']
        ]
        checkout.order_placed = True
        checkout.order_items = ordered_items
        db.session.commit()

    return {"message": "Order placed recorded"}, 200