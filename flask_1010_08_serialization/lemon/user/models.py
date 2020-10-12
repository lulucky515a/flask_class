from werkzeug.security import generate_password_hash, check_password_hash

from lemon.models import Base
from lemon.extensions import db


class User(Base):
    username = db.Column(db.String(20), unique=True, nullable=False, comment="用户名")
    password = db.Column(db.String(512), nullable=False)

    @property
    def pwd(self):
        """原始密码"""
        raise ValueError("不能获取密码")

    @pwd.setter
    def pwd(self, data):
        self.password = generate_password_hash(data)

    def check_password(self, data):
        """校验密码"""
        return check_password_hash(self.password, data)