from flask import Blueprint

# Import the identify_api Blueprint from the identify module
from backend.api.identify.identify_api import identify_api

# Create a parent Blueprint for the entire API
api_blueprint = Blueprint('api', __name__)

# Register the identify_api Blueprint under the /api prefix
api_blueprint.register_blueprint(identify_api, url_prefix='/identify')

# This allows the api_blueprint to be imported and used in the main application
__all__ = ['api_blueprint']
