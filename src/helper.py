from flask import request
from werkzeug.exceptions import BadRequest

def parse_request_data():
    params = {}
    params.update(request.args.to_dict())
    params.update(request.form.to_dict())
    try:
        params.update(request.get_json())
    except BadRequest:
        # Just ignore if request doesn't have json payload
        pass
    return params