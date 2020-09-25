"""配置项。 常量，大写"""
import pathlib


class Config:
    DIR_PATH = pathlib.Path(__file__).resolve().parent
    ROOT_PATH = DIR_PATH.parent
    PATH = ROOT_PATH / 'dev04-dj.db'
    # 数据库设置， URI
    # app.config['SQLALCHEMY_DATABASE_URI'] = r"sqlite:///C:\Users\muji\Desktop\SqlNotes.db"
    SQLALCHEMY_DATABASE_URI = f'sqlite:///{PATH}'
    # 要不要开启 DEBUG
    DEBUG = False
    # secret_key
    SECRET_KEY = 'this is a key'


# 继承
class DevConfig(Config):
    """开发环境"""
    DEBUG = True
    SECRET_KEY = 'Dev Environment'


class ProdConfig(Config):
    """生成环境"""
    pass
