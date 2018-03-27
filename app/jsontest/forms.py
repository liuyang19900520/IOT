# coding=utf-8

from flask_wtf import Form
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
from flask_pagedown.fields import PageDownField
from flask_babel import gettext as _


class Test(Form):
    name = StringField()
    body = PageDownField(label=_(u"正文"), validators=[DataRequired()])
    submit = SubmitField(_(u"发表"))


class CommentForm(Form):
    body = PageDownField(label=_(u'评论'), validators=[DataRequired()])
    submit = SubmitField(_(u'发表'))
