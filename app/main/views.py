# -*- coding: utf-8 -*-
from datetime import datetime
from flask import render_template, request, jsonify
from flask_restful import Resource
from app.models import Post, Comment
from . import main
from .. import api


# from ..models import Post, Comment,CommentSchema

class HelloWorld(Resource):
    def get(self):
        return {'result': 'if you see this page, it means the demo is running without error'}


api.add_resource(HelloWorld, '/')


@main.errorhandler(404)
def page_not_found(error):
    return render_template('404.html'), 404


@main.route('/posts/<user_id>', methods=['POST'])
def insert_post(user_id):
    content = request.get_json()
    post = Post(title=content['title'], user_id=content['user_id'], body=content['body']
                , body_html=content['body_html'], created=datetime.now())
    post.save()
    return jsonify(post)


@main.route('/posts/<user_id>', methods=['GET'])
def select_post_list(user_id):
    posts = Post.objects(user_id=user_id)
    return jsonify(posts)


@main.route('/posts/<user_id>/<post_id>', methods=['GET'])
def select_post_one(user_id, post_id):
    # post = Post.find_one({'_id': ObjectId(post_id)})
    post = Post.objects(pk=post_id)
    return jsonify(post)


@main.route('/posts/<user_id>/<post_id>', methods=['PUT'])
def edit_post(user_id, post_id):
    post = Post.objects(pk=post_id)
    content = request.get_json()
    post.update(title=content['title'], user_id=content['user_id'], body=content['body']
                , body_html=content['body_html'], created=datetime.now())
    return jsonify(post)


@main.route('/posts/<user_id>/<post_id>', methods=['delete'])
def delete_post(post_id):
    post = Post.objects(pk=post_id)
    post.delete()
    return jsonify(post)


@main.route('/posts/<author_id>/<post_id>', methods=['POST'])
def insert_comment(author_id, post_id):
    content = request.get_json()
    comment = Comment(user_id=content['user_id'], body=content['body'], post_id=post_id,
                      created=datetime.now())
    comment.save()
    return jsonify(comment)


@main.route('/posts/<user_id>/<post_id>/comments', methods=['GET'])
def select_comment_list(user_id, post_id):
    comments = Comment.objects(post_id=post_id)
    return jsonify(comments)


@main.route('/posts/<user_id>/<post_id>/comments/<comment_id>', methods=['GET'])
def select_comment_one(user_id, post_id, comment_id):
    comments = Comment.objects(pk=comment_id)
    return jsonify(comments)


@main.route('/posts/<user_id>/<post_id>/comments/<commnent_id>', methods=['PUT'])
def edit_comment(user_id, post_id, commnent_id):
    comment = Comment.objects(pk=commnent_id)
    content = request.get_json()
    comment.update(body=content['body'], created=datetime.now())
    return jsonify(comment)
