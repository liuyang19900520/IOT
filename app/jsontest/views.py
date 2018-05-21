# -*- coding: utf-8 -*-

from flask import render_template, request, flash, redirect, url_for, current_app, abort, jsonify, Response, json
from . import jsont
from .. import db
# from ..models import Post, Comment
from flask.ext.login import login_required, current_user
from flask_babel import gettext as _


@jsont.errorhandler(404)
def page_not_found(error):
    return render_template('404.html'), 404


@jsont.route('/test/json', methods=['GET', 'POST'])
def test():
    username = request.json["name"]
    age=request.json["age"]
    t = {
        'a': username,
        'b': 2,
        'c': [age, 4, 5]
    }
    return jsonify(t)
