from datetime import datetime

from flask import json
from flask_login import UserMixin, AnonymousUserMixin
from flask_marshmallow import Marshmallow
from flask_marshmallow.fields import fields
from markdown import markdown
from sqlalchemy.ext.declarative import DeclarativeMeta

from . import db, login_manager
from flask_mongoengine.wtf import model_form
from wtforms import Form
from wtforms.fields import BooleanField, TextField

# class Role(db.Model):
#     __tablename__ = 'roles'
#     id = db.Column(db.Integer, primary_key=True)
#     name = db.Column(db.String)
#     users = db.relationship('User', backref='role')
#
#     @staticmethod
#     def seed():
#         db.session.add_all(map(lambda r: Role(name=r), ['Guests', 'Administrators']))
#         db.session.commit()
#
#
# class User(UserMixin, db.Model):
#     __tablename__ = 'users'
#     id = db.Column(db.Integer, primary_key=True)
#     name = db.Column(db.String)
#     email = db.Column(db.String)
#     password = db.Column(db.String)
#     role_id = db.Column(db.Integer, db.ForeignKey('roles.id'))
#
#     posts = db.relationship('Post', backref='author')
#     comments = db.relationship('Comment', backref='author')
#
#     locale = db.Column(db.String, default='zh')
#
#     @staticmethod
#     def on_created(target, value, oldvalue, initiator):
#         target.role = Role.query.filter_by(name='Guests').first()
#
#
# class AnonymousUser(AnonymousUserMixin):
#     @property
#     def locale(self):
#         return 'zh'
#
#     def is_administrator(self):
#         return False
#
#
# login_manager.anonymous_user = AnonymousUser
#
#
# @login_manager.user_loader
# def load_user(user_id):
#     return User.query.get(int(user_id))
#
#
# db.event.listen(User.name, 'set', User.on_created)
#
#
# class Post(db.Model):
#     __tablename__ = 'posts'
#     id = db.Column(db.Integer, primary_key=True)
#     title = db.Column(db.String)
#     body = db.Column(db.String)
#     body_html = db.Column(db.String)
#     created = db.Column(db.DateTime, index=True, default=datetime.utcnow)
#
#     comments = db.relationship('Comment', backref='post')
#     author_id = db.Column(db.Integer, db.ForeignKey('users.id'))
#
#     @staticmethod
#     def on_body_changed(target, value, oldvalue, initiator):
#         if value is None or (value is ''):
#             target.body_html = ''
#         else:
#             target.body_html = markdown(value)
#
#
# db.event.listen(Post.body, 'set', Post.on_body_changed)
#
#
# class Comment(db.Model):
#     __tablename__ = 'comments'
#     id = db.Column(db.Integer, primary_key=True)
#     body = db.Column(db.String)
#     created = db.Column(db.DateTime, index=True, default=datetime.utcnow)
#     post_id = db.Column(db.Integer, db.ForeignKey('posts.id'))
#     author_id = db.Column(db.Integer, db.ForeignKey('users.id'))
#
#
# ma = Marshmallow()
#
# class CommentSchema(ma.ModelSchema):
#     class Meta:
#         model = User
#
#     created_at = fields.DateTime('%Y-%m-%dT%H:%M:%S+09:00')
#     author_id = fields.Integer('author_id')
#     body = fields.String('body')
#
#
# class AlchemyEncoder(json.JSONEncoder):
#     def default(self, obj):
#         if isinstance(obj.__class__, DeclarativeMeta):
#             # an SQLAlchemy class
#             fields = {}
#             for field in [x for x in dir(obj) if not x.startswith('_') and x != 'metadata']:
#                 data = obj.__getattribute__(field)
#                 try:
#                     json.dumps(data)  # this will fail on non-encodable values, like other classes
#                     fields[field] = data
#                 except TypeError:
#                     fields[field] = None
#             # a json-encodable dict
#             return fields

class User(db.Document):
    email = db.StringField(required=True)
    first_name = db.StringField(max_length=50)
    last_name = db.StringField(max_length=50)

class Content(db.EmbeddedDocument):
    text = db.StringField()
    lang = db.StringField(max_length=3)

class Post(db.Document):
    title = db.StringField(max_length=120, required=True)
    author = db.ReferenceField(User)
    tags = db.ListField(db.StringField(max_length=30))
    content = db.EmbeddedDocumentField(Content)

class Student(db.Document):
    name=db.StringField(max_length=120, required=True)
    age=db.IntField()