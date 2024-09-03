from flask import Blueprint, render_template
from flask import jsonify
from src.functionality.webhook import checkout_abandoned_handler, \
    order_placed_handler
from src.helper import parse_request_data
from src.utils.enums import Providers
from src.resources.model import Checkout


webhook = Blueprint("webhook", __name__)


@webhook.route("/webhook/<string:provider>/<event>", methods=["POST"])
def webhook_event_handler_api(provider, event):
    request_data = parse_request_data()
    if provider.lower() not in Providers.list():
        return jsonify({"message": "Bad Provider"}), 400
    if event == "checkout_abandoned":
        response, status_code = checkout_abandoned_handler(request_data)
    elif event == "order_placed":
        response, status_code = order_placed_handler(request_data)
    else:
        return jsonify({"message": "Bad event"}), 400
    return jsonify(response), status_code


@webhook.route('/view/messages', methods=['GET'])
def view_messages():
    messages = [
        "Reminder: Complete your purchase!",
        "Still interested?", 
        "Last chance to get your items!"
    ]
    checkouts = Checkout.query.all()
    return render_template('view_messages.html', checkouts=checkouts, messages=messages)