from flask import Blueprint

blueprint = Blueprint("api", __name__, url_prefix="/api")

from app.api import webpage