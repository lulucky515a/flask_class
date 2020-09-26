from lemon.user.blueprint import user_bp
from lemon.user.models import User


@user_bp.route('/login')
def login():
    # 查询所有的 User
    print(User.query.all())
    return {
        "user_id": 2,
        "username": "lucky1",
        "token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyX2lkIjoyLCJ1c2VybmFtZSI6Imx1Y2t5MSIsImV4cCI6MTYwMDkxNDMyNCwiZW1haWwiOiJsdWNreTFAaG90bWFpbC5jb20ifQ.-GzkhGn1U0vX6d2pCBAu1w--EHEXOsL18POGFyXCUSA"
    }


@user_bp.route('/register')
def register():
    return {
        "id": 4,
        "username": "lucky923",
        "token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyX2lkIjo0LCJ1c2VybmFtZSI6Imx1Y2t5OTIzIiwiZXhwIjoxNjAwOTE0MjA0LCJlbWFpbCI6Imx1Y2t5OTIzQGhvdG1haWwuY29tIn0.e4ARMx_JmzCi0AT_tH7PYPZ5hcCgnBgfgJg3Sl89bSo"
    }


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

