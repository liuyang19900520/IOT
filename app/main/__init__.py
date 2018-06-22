# from flask import Blueprint
#
# main = Blueprint('main', __name__)
#
# import app.main.views
from flask import Blueprint
from flask_restful import Api

from .views import Test, PostListApi, PostApi, CommentListApi, CommentApi

main = Blueprint("main", __name__)  # 设置蓝图
resource = Api(main)
resource.add_resource(Test, "/")  # 设置路由
resource.add_resource(PostListApi, "/posts/<string:user_id>", )
resource.add_resource(PostApi, "/posts/<string:user_id>/<string:post_id>")
resource.add_resource(CommentListApi, "/posts/<string:user_id>/<string:post_id>/comments")
resource.add_resource(CommentApi, "/posts/<string:user_id>/<string:post_id>/comments/<string:comment_id>")
