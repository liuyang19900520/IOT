from flask import Blueprint

auth = Blueprint('auth', __name__)

import app.auth.forms, app.auth.views
