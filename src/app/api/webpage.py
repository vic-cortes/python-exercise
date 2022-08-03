from crypt import methods
from flask import request, jsonify

from app.api import blueprint


@blueprint.route("/health", methods=["GET"])
def health():
    return jsonify({"message": "Everything's working fine!"})