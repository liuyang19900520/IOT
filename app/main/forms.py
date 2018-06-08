# coding=utf-8

from flask_mongoengine.wtf import model_form

from ..models import User, Role, Comment, Post

# class PostForm(Form):
#     title = StringField(label=_(u"标题"), validators=[DataRequired()])
#     body = PageDownField(label=_(u"正文"), validators=[DataRequired()])
#     submit = SubmitField(_(u"发表"))
#
#
# class CommentForm(Form):
#     body = PageDownField(label=_(u'评论'), validators=[DataRequired()])
#     submit = SubmitField(_(u'发表'))

PostForm = model_form(Post)
CommentForm = model_form(Comment)
RoleForm = model_form(Role)
UserForm = model_form(User)
