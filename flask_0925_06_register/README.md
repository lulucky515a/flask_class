## 蓝图
- user（权限校验系统）
- project
- iterface
- cases
- env

---------------
蓝图当成是一个可以直接独立配置的功能。
- user
- main(主流程、主应用)—— api_v0
- api_v1
- web  ===> 页面（模板渲染）（）


## 配置文件
- 数据库的访问地址


## 数据库设置，ORM, SQLALCHEMY

- 需要这配置项当中指明数据库的地址
- 初始化 db = SQLALCHEMY()
- 模型类的定义（ORM)  class User
- ORM 模型使用， User.object.all()
- 数据库表关联 ORM 模型类，数据库迁移 flask-migrate


sqlite:
- 数据全部可以存放到一个文件当中 demo.db
- python内置的。不需要任何的安装
- 支持的数据行数还是可以满足很多的项目要求。
- 中小型项目。


# mysql以数据库名称+引擎的方式
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:123@localhost:3306/demo'
SQLALCHEMY_TRACK_MODIFICATIONS = True

# sqlite
app.config['SQLALCHEMY_DATABASE_URI'] = r"sqlite:///C:\Users\muji\Desktop\SqlNotes.db"


## 模型类

- 定义好的模型类，一定要在View 当中使用，否则 flask 发现不了模型类。


## 数据库操作

- flask db init
- flask db migrate
- flask db upgrade


## 开发的流程
- 前端，后端。
- 接口还没有完全都写出来，前端可能没有事情做。
- 前端根据后端提供的接口去开发。

- 先会设计接口。 地址，请求方法，application/json,
- 单打独斗模式：一个一个写，


salt = 'abc'

def generate_password_hash(password):
    """密码"""
    hash = hashlib.sha256()
    hash.update((password + salt).encode('utf-8'))
    return hash.hexdigest()

def check_password(hashpwd, password):
    hash = generate_password_hash(password)
    return hash == hashpwd

