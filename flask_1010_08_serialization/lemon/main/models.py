from lemon.models import Base
from lemon.extensions import db


class Envs(Base):
    name = db.Column(db.String(200), unique=True, comment="环境名称")
    base_url = db.Column(db.String(200), comment="请求base url")
    desc = db.Column(db.String(200), comment="简要描述")


class Projects(Base):
    name = db.Column(db.String(200), unique=True, comment="项目名称")
    leader = db.Column(db.String(50), comment="项目负责人")
    tester = db.Column(db.String(50), comment="项目测试人员")
    programmer = db.Column(db.String(50), comment="开发人员")
    publish_app = db.Column(db.String(100), comment="发布应用")
    # blank null  只对序列化器做校验的时候有用，Projects() & Projects.objects.create() 不起作用
    # desc = models.CharField('简要描述', max_length=200, null=True, blank=True, default='', help_text='简要描述')
    desc = db.Column(db.String(200), default='', comment="简要描述")
    # 关系
    interfaces = db.relationship("Interfaces", backref='project')
    # debugtalks 一对一关系~
    debugtalks = db.relationship("DebugTalks", uselist=False, backref='project')

    def to_json(self):
        return {
            "id": self.id,
            "name": self.name,
            "leader": self.leader,
            "tester": self.tester,
            "programmer": self.programmer,
            "publish_app": self.publish_app,
            "desc": self.desc
        }


class Interfaces(Base):
    name = db.Column(db.String(200), unique=True, comment="接口名称")
    tester = db.Column(db.String(50), comment="测试人员")
    # desc = models.CharField('简要描述', max_length=200, null=True, blank=True, help_text='简要描述')
    desc = db.Column(db.String(200), comment="简要描述")

    # 外键的形式 '表名.字段'
    # 外键，必须要是是唯一键，index, ===> 主键
    # project = models.ForeignKey('projects.Projects', on_delete=models.CASCADE,
    #                                 related_name='interfaces', help_text='所属项目')
    project_id = db.Column(db.ForeignKey("projects.id"), comment="所属项目")

    testcases = db.relationship("Testcases", backref='interface')
    configs = db.relationship("Configures", backref='interface')


class Configures(Base):
    name = db.Column(db.String(50), comment="配置名称")
    # interfaces 外键关联 ??? on_delete=models.CASCADE
    #     interface = models.ForeignKey('interfaces.Interfaces',
    #                                   on_delete=models.CASCADE,
    #                                   related_name='configures',
    #                                   help_text='所属接口')
    interface_id = db.Column(db.ForeignKey("interfaces.id"), comment="所属接口")

    author = db.Column(db.String(50), comment="编写人员")
    request = db.Column(db.Text, comment="请求信息")


class DebugTalks(Base):
    name = db.Column(db.String(200), default='debugtalk.py', comment="debugtalk文件名称")
    debugtalk = db.Column(db.Text, default='#debugtalk.py', comment="debugtalk.py文件")

    # projects 外键关联 ??? on_delete=models.CASCADE
    # project = db.OneToOneField('projects.Projects', on_delete=models.CASCADE,
    #                                related_name='debugtalks', help_text='所属项目')
    project_id = db.Column(db.ForeignKey("projects.id"), comment="所属项目")


class Reports(Base):
    name = db.Column(db.String(200), unique=True, comment="报告名称")
    result = db.Column(db.SmallInteger, default=1, comment='执行结果')  # 1为成功, 0为失败 default=1,
    count = db.Column(db.Integer, comment='总用例数')
    success = db.Column(db.Integer, comment='成功总数')
    # blank=True ???
    # html = models.TextField('报告HTML源码', help_text='报告HTML源码', null=True, blank=True, default='')
    html = db.Column(db.Text, default='', comment='报告HTML源码')
    # summary = models.TextField('报告详情', help_text='报告详情', null=True, blank=True, default='')
    summary = db.Column(db.Text, default='', comment='报告详情')


class Summary(Base):
    user = db.Column(db.String(200), unique=True, comment="用户名称")
    statistics = db.Column(db.Integer, comment='测试信息')


class Testcases(Base):
    name = db.Column(db.String(50), unique=True, comment="用例名称")

    # interfaces 外键关联 ??? on_delete=models.CASCADE
    # interface = models.ForeignKey('interfaces.Interfaces', on_delete=models.CASCADE, related_name='testcases',
    #                               help_text='所属接口')
    interface_id = db.Column(db.ForeignKey("interfaces.id"), comment="所属接口")

    include = db.Column(db.String(50), comment='用例执行前置顺序')
    author = db.Column(db.String(50), comment='编写人员')
    request = db.Column(db.String(50), comment='请求信息')


class Testsuits(Base):
    name = db.Column(db.String(200), unique=True, comment="套件名称")

    # project 外键关联 ??? on_delete=models.CASCADE
    # project = models.ForeignKey('projects.Projects', on_delete=models.CASCADE,
    #                                 related_name='testsuits', help_text='所属项目')
    project_id = db.Column(db.ForeignKey("projects.id"), comment="所属项目")

    include = db.Column(db.Text, comment='包含的接口')