from lemon.models import Base
from lemon.extensions import db


class Envs(Base):
    name = db.Column(db.String(200), unique=True, comment="环境名称")
    base_url = db.Text(db.String(200))
    desc = db.Column(db.String(200), comment="简要描述")


class Projects(Base):
    """项目的结构。 字段保持一致。"""
    name = db.Column(db.String(200), unique=True, comment="项目名称")
    leader = db.Column(db.String(50), comment="项目负责人")
    tester = db.Column(db.String(50), comment="项目测试人员")
    programmer = db.Column(db.String(50), comment="开发人员")
    publish_app = db.Column(db.String(100), comment="发布应用")
    desc = db.Column(db.String(200), nullable=True, default='', comment="简要描述")


class Interfaces(Base):
    name = db.Column(db.String(200), unique=True, comment="接口名称")
    # project外键关联 ???
    # project = db.ForeignKey('project.Projects', on_delete=Projects.CASCADE, comment="所属项目")

    tester = db.Column(db.String(50), comment="测试人员")
    desc = db.Column(db.String(200), nullable=True, default='', comment="简要描述")


class Configures(Base):
    name = db.Column(db.String(50), unique=True, comment="配置名称")
    # interfaces 外键关联 ??? on_delete=models.CASCADE
    # interface = db.ForeignKey('interfaces.Interfaces',
    #                           on_delete=Interfaces.CASCADE,
    #                           related_name='configures',
    #                           comment="所属接口")

    author = db.Column(db.String(50), comment="编写人员")
    request = db.Text()

    # interface = models.ForeignKey('interfaces.Interfaces',
    #                               on_delete=models.CASCADE,
    #                               related_name='configures',
    #                               help_text='所属接口')


class DebugTalks(Base):
    name = db.Column(db.String(200), default='debugtalk.py', comment="debugtalk文件名称")
    debugtalk = db.Column(nullable=True, default='#debugtalk.py')

    # projects 外键关联 ??? on_delete=models.CASCADE
    # project = db.OneToOneField('projects.Projects', on_delete=models.CASCADE,
    #                                related_name='debugtalks', help_text='所属项目')

class Reports(Base):
    name = db.Column(db.String(200), unique=True, comment="报告名称")
    result = db.Boolean()  # 1为成功, 0为失败 default=1,
    count = db.Integer()
    success = db.Integer()
    # blank=True ???
    html = db.Text()
    summary = db.Text()


class Summary(Base):
    user = db.Column(db.String(200), unique=True, comment="用户名称")
    statistics = db.Integer()


class Testcases(Base):
    name = db.Column(db.String(50), unique=True, comment="用例名称")

    # interfaces 外键关联 ??? on_delete=models.CASCADE
    # interface = models.ForeignKey('interfaces.Interfaces', on_delete=models.CASCADE, related_name='testcases',
    #                               help_text='所属接口')

    include = db.Text()
    author = db.Column(db.String(50), comment='编写人员')
    request = db.Text()


class Testsuits(Base):
    name = db.Column(db.String(200), unique=True, comment="套件名称")

    # project 外键关联 ??? on_delete=models.CASCADE
    # project = models.ForeignKey('projects.Projects', on_delete=models.CASCADE,
    #                                 related_name='testsuits', help_text='所属项目')

    include = db.Text()