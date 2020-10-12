# 初始化 app 对象
from flask import Flask
from marshmallow import ValidationError

from lemon import views, config, config_pathlib
from lemon.extensions import db, migrate, jwt, cors, ma
from lemon.user import user_bp
from lemon.user.models import User
from lemon.main import main_bp, views
from lemon import error_handler


app = Flask(__name__)
# 有没有加载路由

# 循环导入
# from lemon import views


def register_view(app: Flask):
    """注册路由"""
    # app.add_url_rule('/', view_func=views.index)
    app.add_url_rule('/projects', view_func=views)


def register_blueprints(app: Flask):
    """注册蓝图"""
    # 注册
    app.register_blueprint(user_bp)
    app.register_blueprint(main_bp)


def register_extensions(app: Flask):
    """注册插件"""
    db.init_app(app)
    migrate.init_app(app, db=db)
    jwt.init_app(app)
    cors.init_app(app)
    ma.init_app(app)

    @jwt.user_loader_callback_loader
    def user_loader_callback(identity):
        user= User.query.filter_by(username=identity).first()
        if user:
            return user


def register_error(app):
    app.register_error_handler(ValidationError, error_handler.validation_handler)
    app.register_error_handler(404, error_handler.not_found)
    app.register_error_handler(500, error_handler.server_error)
    app.register_error_handler(ZeroDivisionError, error_handler.zero_error_handler)
    # pass


def create_app(setting=None):
    """初始化app的各项功能, 生成、组装 app 的工厂"""

    # if setting:
    #     app.config.from_object(config_pathlib.DevConfig)
    # else:
    #     app.config.from_object(config_pathlib.ProdConfig)

    app.config.from_object(config_pathlib.DevConfig) if config else app.config.from_object(config_pathlib.ProdConfig)

    register_blueprints(app)
    register_view(app)
    register_extensions(app)
    register_error(app)
    return app