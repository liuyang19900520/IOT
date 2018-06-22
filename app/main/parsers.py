# coding=utf-8
from flask_restful import inputs
from flask_restful.reqparse import RequestParser

from ..models import Post

parser = RequestParser()
parser.add_argument("user_id", type=str, required=True)
parser.add_argument("post_id", type=str)
parser.add_argument("comment_id", type=str)

parser.add_argument("title", type=str, required=True)
parser.add_argument("body", type=str)
parser.add_argument("body_html", type=str)

