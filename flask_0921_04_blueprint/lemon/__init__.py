# 初始化 app 对象
from flask import Flask

from lemon import views, conf_module
from lemon.user import user_bp

app = Flask(__name__)
# 有没有加载路由

# 循环导入
# from lemon import views


def register_view(app: Flask):
    """注册路由"""
    app.add_url_rule('/', view_func=views.index)


def register_blueprints(app: Flask):
    """注册蓝图"""
    # 注册
    app.register_blueprint(user_bp)


def create_app(config=None):
    """初始化app的各项功能, 生成、组装 app 的工厂"""

    if config:
        app.config.from_object(conf_module.ProConfig)

    register_blueprints(app)
    register_view(app)


    return app