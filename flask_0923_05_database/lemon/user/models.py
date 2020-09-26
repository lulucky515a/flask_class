from lemon.models import Base
from lemon.extensions import db


class User(Base):
    username = db.Column(db.String(20), unique=True, nullable=False, comment="用户名")
    password = db.Column(db.String(512), nullable=False)