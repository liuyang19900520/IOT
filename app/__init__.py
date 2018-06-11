# coding: utf-8

from os import path

from flask import Flask, request
from flask_babel import Babel
from flask_bootstrap import Bootstrap
from flask_gravatar import Gravatar
from flask_login import LoginManager, current_user
from flask_mongoengine import MongoEngine
from flask_pagedown import PageDown
from flask_restful import Api

from config import config

basedir = path.abspath(path.dirname(__file__))

db = MongoEngine()
babel = Babel()
bootstrap = Bootstrap()
pagedown = PageDown()
login_manager = LoginManager()
login_manager.session_protection = 'strong'
login_manager.login_view = 'auth.login'
api = Api()


def create_app(config_name='default'):
    app = Flask(__name__)
    app.debug = True
    app.config.from_object(config[config_name])
    db.init_app(app)
    bootstrap.init_app(app)
    login_manager.init_app(app)
    pagedown.init_app(app)

    babel.init_app(app)
    Gravatar(app, size=64)

    from app.auth import auth as auth_blueprint
    from app.main import main as main_blueprint

    app.register_blueprint(auth_blueprint, url_prefix='/auth')
    app.register_blueprint(main_blueprint, static_folder='static')
    api.init_app(app)

    @app.template_test('current_link')
    def is_current_link(link):
        return link == request.path

    @babel.localeselector
    def get_locale():
        return current_user.locale

    return app
