# coding:utf-8
# error
from flask import Blueprint, render_template, redirect, session, request, abort, jsonify, json

from app import make_result

exception = Blueprint('exception', __name__)


class ApiException(Exception):
    """将本地错误包装成一个异常实例供抛出"""

    def __init__(self, message, data):
        self.message = message
        self.data = data
        self.code = 1


@exception.app_errorhandler(ApiException)
def handle_bad_request(error):
    """捕获 BadRequest 全局异常，序列化为 JSON 并返回 HTTP 400"""
    return make_result(code=1, msg=error.message, data=error.data)


@exception.app_errorhandler(404)
def handle_bad_request_404(error):
    """捕获 BadRequest 全局异常，序列化为 JSON 并返回 HTTP 400"""

    return make_result(code=1, msg=str(error)), 404


@exception.app_errorhandler(500)
def handle_bad_request_500(error):
    """捕获 BadRequest 全局异常，序列化为 JSON 并返回 HTTP 400"""
    return make_result(code=1, msg=str(error)), 500
