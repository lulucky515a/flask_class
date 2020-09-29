from datetime import datetime

from lemon.extensions import db


class Base(db.Model):
    # 指定在迁移时不创建表
    __abstract__ = True

    id = db.Column(db.Integer, primary_key=True)
    status = db.Column(db.SmallInteger, nullable=False, default=0)
    created_at = db.Column(db.DateTime, default=datetime.now())
    updated_at = db.Column(db.DateTime, default=datetime.now(), onupdate=datetime.now())

    def save(self):
        """保存数据"""
        try:
            db.session.add(self)
            db.session.commit()
            return self
        except:
            # 数据回滚
            # 记录日志
            # 抛出异常。
            db.session.rollback()