from flask import request, jsonify

from app.api import blueprint
from app.controller import webpage as webpage_controller


@blueprint.route("/health", methods=["GET"])
def health():
    return jsonify({"message": "Everything's working fine!"})


@blueprint.route("/retrieve/metadata", methods=["POST"])
def metadata():
    json_data = request.get_json(force=True)
    url = json_data.get("url")

    valid, data = webpage_controller.get_webpage(webpage=url)

    if not valid:
        message = f"Data not available for url {url}"
        return jsonify({"message": message}), 400

    message_response = {"url": url, "status": "SUCCESS", "data": data}

    return jsonify(message_response)
