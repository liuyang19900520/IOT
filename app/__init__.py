# coding: utf-8

from os import path

import flask_restful
from flask import Flask
from flask_babel import Babel
from flask_bootstrap import Bootstrap
from flask_gravatar import Gravatar
from flask_login import LoginManager
from flask_mongoengine import MongoEngine
from flask_pagedown import PageDown
from flask_restful import abort

from app.utils import make_result
from config import config

basedir = path.abspath(path.dirname(__file__))

db = MongoEngine()
babel = Babel()
bootstrap = Bootstrap()
pagedown = PageDown()
login_manager = LoginManager()
login_manager.session_protection = 'strong'
login_manager.login_view = 'auth.login'


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
    from app.exception import exception as exception_blueprint

    app.register_blueprint(auth_blueprint, url_prefix='/auth')
    app.register_blueprint(main_blueprint, static_folder='static')
    app.register_blueprint(exception_blueprint)

    def custom_abord(http_status_code, *args, **kwargs):
        # 只要http_status_code 为400， 报参数错误
        if http_status_code == 400:
            abort(make_result(code=400, msg="400"))
        if http_status_code == 404:
            abort(make_result(code=404, msg="404"))
        # 正常返回消息
        return abort(http_status_code)

    flask_restful.abort = custom_abord

    return app
