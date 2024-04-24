from flask import Blueprint
from flasgger import Swagger

swagger_bp = Blueprint('swagger', __name__)

Swagger(app)