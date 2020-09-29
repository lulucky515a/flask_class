from flask import request
from flask_jwt_extended import create_access_token
from werkzeug.security import generate_password_hash

from lemon.user.blueprint import user_bp
from lemon.user.models import User


@user_bp.route('/login/', methods=['POST'])
def login():
    req_data = request.json
    username = req_data.get("username", "")
    password = req_data.get("password", "")

    user = User.query.filter_by(username=username).first()
    if not user:
        return {"msg": "no user"}

    # 判断密码
    if not user.check_password(password):
        return {"msg": "error password"}
    # 创建一个使用user.name 进行加密的token
    token = create_access_token(identity=user.username)

    return {
        "user_id": user.id,
        "username": user.username,
        "token": token
    }


@user_bp.route('/register/', methods=['POST'])
def register():
    # 接收用户数据
    req_data = request.json
    username = req_data.get("username", "")
    password = req_data.get("password", "")

    # ------ 第一种：使用generate_password_hash ------
    """
    # 密码加密的字段
    # 不要在view里面做过多的操作，可以封装到models中
    # pwd_hash = generate_password_hash(password)

    # 保存用户名和密码
    user = User(username=username, password=pwd_hash)
    """

    # ------ 第二种：在models中定义类属性 ------
    # 保存用户名和密码
    user = User(username=username)
    user.pwd = password

    # 应不应该，得到原始密码
    # # user.pwd
    user.save()

    # 生成 token: 由什么原始数据生成。
    token = create_access_token(identity=user.username)

    return {
        "id": user.id,
        "username": user.username,
        "token": token
    }
    # return {
    #     "id": 4,
    #     "username": "lucky923",
    #     "token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyX2lkIjo0LCJ1c2VybmFtZSI6Imx1Y2t5OTIzIiwiZXhwI
    #     joxNjAwOTE0MjA0LCJlbWFpbCI6Imx1Y2t5OTIzQGhvdG1haWwuY29tIn0.e4ARMx_JmzCi0AT_tH7PYPZ5hcCgnBgfgJg3Sl89bSo"
    # }


@user_bp.route('/<username>/count/')
def username(username):
    return {
        "username": f"{username}",
        "count": 1
    }


@user_bp.route('/<email>/count/')
def email(email):
    return {
        "email": f"{email}@hotmail.com",
        "count": 1
    }

