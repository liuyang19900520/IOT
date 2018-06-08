# -*- coding: utf-8 -*-
from datetime import datetime

from flask import render_template, request, jsonify

from app.models import Post, Comment
from . import main


# from ..models import Post, Comment,CommentSchema


@main.errorhandler(404)
def page_not_found(error):
    return render_template('404.html'), 404


# @main.route('/')
# def index():
#     # posts=Post.query.all()
#
#     page_index = request.args.get('page', 1, type=int)
#
#     query = Post.query.order_by(Post.created.desc())
#
#     pagination = query.paginate(page_index, per_page=20, error_out=False)
#
#     posts = pagination.items
#
#     return render_template('index.html',
#                            title=_(u'欢迎来到LiuYang的博客'),
#                            posts=posts,
#                            pagination=pagination)
#
#
# @main.route('/about')
# def about():
#     return render_template('about.html', title=u'关于')
#
#
# @main.route('/posts/<int:id>', methods=['GET', 'POST'])
# def post(id):
#     # Detail 详情页
#     post = Post.query.get_or_404(id)
#
#     # 评论窗体
#     form = CommentForm()
#
#     # 保存评论
#     if form.validate_on_submit():
#         comment = Comment(author=current_user,
#                           body=form.body.data,
#                           post=post)
#         db.session.add(comment)
#         db.session.commit()
#
#     return render_template('posts/detail.html',
#                            title=post.title,
#                            form=form,
#                            post=post)
#
#
# @main.route('/edit', methods=['GET', 'POST'])
# @main.route('/edit/<int:id>', methods=['GET', 'POST'])
# @login_required
# def edit(id=0):
#     form = PostForm()
#
#     if id == 0:
#         post = Post(author=current_user)
#     else:
#         post = Post.query.get_or_404(id)
#
#     if form.validate_on_submit():
#         post.body = form.body.data
#         post.title = form.title.data
#
#         db.session.add(post)
#         db.session.commit()
#
#         return redirect(url_for('.post', id=post.id))
#
#     form.title.data = post.title
#     form.body.data = post.body
#
#     title = _(u'添加新文章')
#     if id > 0:
#         title = _(u'编辑 - %(title)', title=post.title)
#
#     return render_template('posts/edit.html',
#                            title=title,
#                            form=form,
#                            post=post)
#
#
# @main.route('/shoutdown')
# def shutdown():
#     if not current_app.testing:
#         abort(404)
#
#     shoutdown = request.environ.get('werkzeug.server.shutdown')
#     if not shoutdown:
#         abort(500)
#
#     shoutdown()
#     return u'正在关闭服务端进程...'
#
#
# #####################################################################################
# @main.route('/article/<int:id>', methods=['GET', 'POST'])
# def article(id):
#     # Detail 详情页
#     post = Post.query.get_or_404(id)
#
#     # 评论窗体
#     form = CommentForm()
#
#     # 保存评论
#     if form.validate_on_submit():
#         comment = Comment(author=current_user,
#                           body=form.body.data,
#                           post=post)
#         db.session.add(comment)
#         db.session.commit()
#
#     t = {
#         'title': post.title,
#         'author': post.author_id,
#         'content': post.body,
#          'comments': CommentSchema(many=True).dump(post.comments)
#     }
#     return jsonify(t)
# @main.route('/post', methods=['POST'])
# def add_post():
#     content = request.get_json()
#     print(content)
#     post = Post(author_id=content['author_id'])
#     post.save()
#     return "ok"
#     return "ok"


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
def select_comment_list(user_id,post_id):
    comments = Comment.objects(post_id=post_id)
    return jsonify(comments)

@main.route('/posts/<user_id>/<post_id>/comments/<comment_id>', methods=['GET'])
def select_comment_one(user_id,post_id,comment_id):
    comments = Comment.objects(pk=comment_id)
    return jsonify(comments)

@main.route('/posts/<user_id>/<post_id>/comments/<commnent_id>', methods=['PUT'])
def edit_comment(user_id, post_id,commnent_id):
    comment = Comment.objects(pk=commnent_id)
    content = request.get_json()
    comment.update( body=content['body'], created=datetime.now())
    return jsonify(comment)

