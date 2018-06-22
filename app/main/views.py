# -*- coding: utf-8 -*-
from datetime import datetime

from bson import objectid
from flask.json import jsonify
from flask_restful import Resource

from app.exception import ApiException
from app.models import Post, Comment
from .parsers import parser
from ..utils import make_result


class Test(Resource):
    def get(self):
        return make_result(data="this is the right response")


class PostListApi(Resource):
    def get(self, user_id):
        posts = Post.objects(user_id=user_id)
        return make_result(data=posts)

    def post(self, user_id):
        args = parser.parse_args()
        new_post = Post(title=args['title'], user_id=user_id, body=args['body']
                        , body_html=args['body_html'], created=datetime.now())
        new_post.save()
        return make_result(data=new_post)


class PostApi(Resource):
    def get(self, user_id, post_id):
        if objectid.ObjectId.is_valid(post_id):
            post = Post.objects(pk=post_id)
            return make_result(data=post)
        else:
            raise ApiException('post_id is not correct', post_id)

    def put(self, user_id, post_id):
        if objectid.ObjectId.is_valid(post_id):
            post = Post.objects(pk=post_id)
            content = parser.parse_args()
            post.update(title=content['title'], user_id=content['user_id'], body=content['body']
                        , body_html=content['body_html'], created=datetime.now())
            return make_result(data=post)
        else:
            raise ApiException('post_id is not correct', post_id)

    def delete(self, user_id, post_id):
        if objectid.ObjectId.is_valid(post_id):
            post = Post.objects(pk=post_id)
            post.delete()
            return make_result(data=post)
        else:
            raise ApiException('post_id is not correct', post_id)


class CommentListApi(Resource):
    def get(self, user_id, post_id):
        if objectid.ObjectId.is_valid(post_id):
            comments = Comment.objects(post_id=post_id)
            return make_result(data=comments)
        else:
            raise ApiException('post_id is not correct', post_id)

    def post(self, user_id, post_id):
        if objectid.ObjectId.is_valid(post_id):
            content = parser.parse_args()
            comment = Comment(user_id=content['user_id'], body=content['body'], post_id=post_id,
                              created=datetime.now())
            comment.save()
            return make_result(data=comment)
        else:
            raise ApiException('post_id is not correct', post_id)


class CommentApi(Resource):

    def get(self, user_id, post_id, comment_id):
        if objectid.ObjectId.is_valid(post_id) & objectid.ObjectId.is_valid(comment_id):
            comment = Comment.objects(pk=comment_id)
            return make_result(data=comment)
        else:
            if objectid.ObjectId.is_valid(post_id):
                raise ApiException('comment_id is not correct', comment_id)
            if objectid.ObjectId.is_valid(comment_id):
                raise ApiException('post_id is not correct', post_id)
            else:
                raise ApiException('post_id and comment_id are not correct',
                                   {'post': post_id, 'comment': comment_id})

    def post(self, user_id, post_id, comment_id):
        if objectid.ObjectId.is_valid(post_id) & objectid.ObjectId.is_valid(comment_id):
            comment = Comment.objects(pk=comment_id)
            content = parser.parse_args()
            comment.update(body=content['body'], created=datetime.now())
            return make_result(data=comment)
        else:
            if objectid.ObjectId.is_valid(post_id):
                raise ApiException('comment_id is not correct', comment_id)
            if objectid.ObjectId.is_valid(comment_id):
                raise ApiException('post_id is not correct', post_id)
            else:
                raise ApiException('post_id and comment_id are not correct',
                                   {'post': post_id, 'comment': comment_id})

    def delete(self, user_id, post_id, comment_id):
        if objectid.ObjectId.is_valid(post_id) & objectid.ObjectId.is_valid(comment_id):
            comment = Post.objects(pk=comment_id)
            comment.delete()
            return make_result(data=comment)
        else:
            if objectid.ObjectId.is_valid(post_id):
                raise ApiException('comment_id is not correct', comment_id)
            if objectid.ObjectId.is_valid(comment_id):
                raise ApiException('post_id is not correct', post_id)
            else:
                raise ApiException('post_id and comment_id are not correct',
                                   {'post': post_id, 'comment': comment_id})
# class HelloWorld(Resource):
#     def get(self):
#         return {'result': 'if you see this page, it means the demo is running without error'}
#
#
# api.add_resource(HelloWorld, '/')

#
# @main.errorhandler(InvalidUsage)
# def invalid_usage(error):
#     parser = reqparse.RequestParser()
#     parser.add_argument(
#         'foo',
#         choices=('one', 'two'),
#         help='Bad choice: {error_msg}'
#     )
#     return parser
#
#
# @main.route('/posts/<user_id>', methods=['POST'])
# def insert_post(user_id):
#     content = request.get_json()
#     post = Post(title=content['title'], user_id=content['user_id'], body=content['body']
#                 , body_html=content['body_html'], created=datetime.now())
#     post.save()
#     return jsonify(post)
#
#
# @main.route('/posts/<user_id>', methods=['GET'])
# def select_post_list(user_id):
#     posts = Post.objects(user_id=user_id)
#     return jsonify(posts)
#
#
# @main.route('/posts/<user_id>/<post_id>', methods=['GET'])
# def select_post_one(user_id, post_id):
#     # post = Post.find_one({'_id': ObjectId(post_id)})
#     post = Post.objects(pk=post_id)
#     return jsonify(post)
#
#
# @main.route('/posts/<user_id>/<post_id>', methods=['PUT'])
# def edit_post(user_id, post_id):
#     post = Post.objects(pk=post_id)
#     content = request.get_json()
#     post.update(title=content['title'], user_id=content['user_id'], body=content['body']
#                 , body_html=content['body_html'], created=datetime.now())
#     return jsonify(post)
#
#
# @main.route('/posts/<user_id>/<post_id>', methods=['delete'])
# def delete_post(post_id):
#     post = Post.objects(pk=post_id)
#     post.delete()
#     return jsonify(post)
#
#
# @main.route('/posts/<author_id>/<post_id>', methods=['POST'])
# def insert_comment(author_id, post_id):
#     content = request.get_json()
#     comment = Comment(user_id=content['user_id'], body=content['body'], post_id=post_id,
#                       created=datetime.now())
#     comment.save()
#     return jsonify(comment)
#
#
# @main.route('/posts/<user_id>/<post_id>/comments', methods=['GET'])
# def select_comment_list(user_id, post_id):
#     comments = Comment.objects(post_id=post_id)
#     return jsonify(comments)
#
#
# @main.route('/posts/<user_id>/<post_id>/comments/<comment_id>', methods=['GET'])
# def select_comment_one(user_id, post_id, comment_id):
#     comments = Comment.objects(pk=comment_id)
#     return jsonify(comments)
#
#
# @main.route('/posts/<user_id>/<post_id>/comments/<commnent_id>', methods=['PUT'])
# def edit_comment(user_id, post_id, commnent_id):
#     comment = Comment.objects(pk=commnent_id)
#     content = request.get_json()
#     comment.update(body=content['body'], created=datetime.now())
#     return jsonify(comment)
