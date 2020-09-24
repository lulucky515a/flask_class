from lemon.models import Base
from lemon.extensions import db


class Projects(Base):
    """项目的结构。 字段保持一致。"""
    name = db.Column(db.String(200), unique=True)
    leader = db.Column(db.String(50))
    tester = db.Column(db.String(50))
    programmer = db.Column(db.String(50))
    publish_app = db.Column(db.String(100))
    desc = db.Column(db.String(200))


class Interfaces(Base):
    """项目的结构。 字段保持一致。"""
    name = db.Column(db.String(200), unique=True)
    # project外键关联
    project = db.ForeignKey('project.Projects',ondelete=db.CASCADE)

    tester = db.Column(db.String(50))
    desc = db.Column(db.String(200))