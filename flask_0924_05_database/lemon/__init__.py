# 初始化 app 对象
from flask import Flask

from lemon import views, config
from lemon.extensions import db, migrate
from lemon.user import user_bp
from lemon.main import main_bp, views


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


def create_app(config=None):
    """初始化app的各项功能, 生成、组装 app 的工厂"""

    # if config:
    #     app.config.from_object(config.DevConfig)

    register_blueprints(app)
    register_view(app)



    return app