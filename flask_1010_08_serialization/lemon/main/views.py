# -*- coding: UTF-8 -*-
# 当前项目的名称: flask_class 
# 新文件名称：views 
# 当前登录名：LuckyLu
# 创建日期：2020/9/24 10:42
# 文件IDE名称：PyCharm

from flask import request, abort
from flask.views import MethodView
from flask_jwt_extended import jwt_required, get_jwt_identity, current_user
from sqlalchemy.orm import Query
from flask.json import jsonify

from lemon.main.bluerpint import main_bp
from lemon.main.models import Projects, Interfaces, Configures, DebugTalks, Envs, Reports, Summary, Testcases, Testsuits
from lemon.main import serialization as se


"""
有问题
蓝图的views里面使用类视图实现接口编写，
那project的二级url地址是要用app.add_url_rule('/names', view_func=ProjectView.as_view('project'))去指定，
然后project接口地址在__init__里面进行路由注册，蓝图好像没啥用了啊，但是用装饰器的话，函数又太多了，毕竟那么多接口

class ProjectView(MethodView):
    # 实现指定的 methods 类属性，照样可以控制请求方法。
    # 就算类当中实现了 实例方法 get, post, 也是不支持对应的请求方法的。
    # methods = ['GET']


    # def list(self):
    #     return {
    #     "count": 1,
    #     "next": None,
    #     "previous": None,
    #     "results": [
    #         {
    #             "id": 1,
    #             "create_time": "2020年09月15日 11:25:16",
    #             "name": "pa",
    #             "leader": "ld",
    #             "tester": "lucky",
    #             "programmer": "dev",
    #             "publish_app": "sandbox",
    #             "desc": "sandbox",
    #             "interfaces": 0,
    #             "testcases": 0,
    #             "testsuits": 0,
    #             "configures": 0
    #         }
    #     ],
    #     "current_page_num": 1,
    #     "total_pages": 1
    # }

    def get(self):
        return [
            {
                "id": 1,
                "name": "pa"
            }
        ]


    def post(self):
        return "method post project"

    def put(self):
        return "method put project"

# 注册视图
# 基于类的视图，不要用装饰器，采取集中注册的形式，add_url_rule
# TODO: PR
# app.add_url_rule('/', view_func=ProjectView.as_view('projects'))
# app.add_url_rule('/names', view_func=ProjectView.as_view('projects'))
"""


@main_bp.route('/you', methods=['GET'])
def hello():
    class A:
        pass
    a = A()
    1 / 0
    # ORM 对象
    # project/1 ==> {}
    return a


# ------ envs ------
@main_bp.route('/envs/', methods=['GET'])
def envs_list():
    envs_obj = Envs.query.all()

    # 序列化 projects ==> json
    schema = se.EnvsSchema(many=True, exclude=['status', 'updated_at'])
    envs_json = schema.dump(envs_obj)
    return {"results": envs_json}

    # return {"result": [env.name for env in envs_obj]}


@main_bp.route('/envs/', methods=['POST'])
def envs_create():
    """
    # ------ 手动获取数据进行处理 ------
    req_data = request.json
    # {"name": "", "tester": "", "programmer": ""}
    envs = Envs(**req_data)
    # 把你要提交的需要存储的数据放到 session
    # db.session.add(project)
    # # 提交事务
    # db.session.commit()
    envs.save()
    return {'result': envs.name}
    """

    # 从客户端接收数据
    req_data = request.json
    # 初始化序列化器
    schema = se.EnvsSchema()
    # 反序列化, 还是一个字典（校验的过程）
    env = schema.load(req_data)
    # return project
    # return {"result": "project1"}
    # 序列化输出
    schema_out = se.EnvsSchema(exclude=['status', 'updated_at'])
    env_json = schema_out.dump(env)
    return jsonify(env_json)


@main_bp.route('/envs/names/', methods=['GET'])
def envs_names():
    envs = Envs.query.all()
    schema = se.EnvsSchema(many=True, only=['id', 'name'])
    envs_json = schema.dump(envs)
    return jsonify(envs_json)


@main_bp.route('/envs/<id>/', methods=['GET'])
def envs_read(id):
    env = Envs.query.get(id)
    schema = se.EnvsSchema(exclude=['status', 'updated_at'])
    env_json = schema.dump(env)

    # 序列化 projects ==> json
    return jsonify(env_json)


@main_bp.route('/envs/<id>/', methods=['PUT'])
def envs_update(id):
    return {"envs_update": f"{id}"}


@main_bp.route('/envs/<id>/', methods=['PATCH'])
def envs_partial_update(id):
    return {"envs_partial_update": f"{id}"}


@main_bp.route('/envs/<id>/', methods=['DELETE'])
def envs_delete(id):
    return {"envs_delete": f"{id}"}


# ------ 手工处理接收的数据 ------
"""
@main_bp.route('/projects/', methods=['GET'])
@jwt_required
def projects_list():
    # 获取用户信息
    username = get_jwt_identity()
    # print(username)
    # user = User.query.filter_by(username=username).first()

    print(current_user)

    # 获取所有的 Projects 数据
    # 数据筛选, 关键字参数必须是 Project 模型当中的数据字段的名称
    # Projects.query.filter(Projects.name == '自动化测试平台项目')
    # Projects.query.filter_by(name='自动化测试平台项目').all()
    projects = Projects.query.all()

    print(projects)

    # 序列化 projects ==> json
    # return jsonify(projects)

    return {"result": [project.to_json() for project in projects]}

    # return {"results": [project.id for project in projects]}
"""

# ------ 使用marshmallow序列化输出的数据 ------
@main_bp.route('/projects/', methods=['GET'])
@jwt_required
def projects_list():
    # 列表
    projects = Projects.query.all()
    schema = se.ProjectsSchema(many=True, exclude=['status', 'updated_at'])
    projects_json = schema.dump(projects)
    return {"results": projects_json}


# ------ 手工处理接收的数据 ------
"""
@main_bp.route('/projects/', methods=['POST'])
def projects_create():
    # 创建 Project 对象，保存
    # 生成 Project
    # 获取从传递过来的数据
    req_data = request.json
    # {"name": "", "tester": "", "programmer": ""}
    project = Projects(**req_data)
    # 把你要提交的需要存储的数据放到 session
    # db.session.add(project)
    # # 提交事务
    # db.session.commit()
    project.save()
    return {'result': project.id}
    # return {"result": "projects_create"}
"""

# ------ 使用marshmallow反序列化接收的数据 ------
@main_bp.route('/projects/', methods=['POST'])
# @jwt_required
def projects_create():
    # abort(404)
    # 从客户端接收数据
    req_data = request.json
    # 初始化序列化器
    schema = se.ProjectsSchema()
    # 反序列化, 还是一个字典（校验的过程）
    project = schema.load(req_data)
    # return project
    # return {"result": "project1"}
    # 序列化输出
    schema_out = se.ProjectsSchema(exclude=['status', 'updated_at'])
    projects_json = schema_out.dump(project)
    return projects_json


@main_bp.route('/projects/names/', methods=['GET'])
def projects_names():
    projects = Projects.query.all()
    schema = se.ProjectsSchema(many=True, only=['id', 'name'])
    projects_json = schema.dump(projects)

    # 序列化 projects ==> json
    # return {"result": [project.name for project in projects]}
    return jsonify(projects_json)


@main_bp.route('/projects/<id>/', methods=['GET'])
def projects_read(id):
    project = Projects.query.get(id)
    schema = se.ProjectsSchema(exclude=['status', 'updated_at'])
    project_json = schema.dump(project)

    # 序列化 projects ==> json
    # return {"result": [project.name for project in projects]}
    return jsonify(project_json)


@main_bp.route('/projects/<id>/', methods=['PUT'])
def projects_update(id):
    return {"projects_update": f"{id}"}


@main_bp.route('/projects/<id>/', methods=['PATCH'])
def projects_partial_update(id):
    return {"projects_partial_update": f"{id}"}


@main_bp.route('/projects/<id>/', methods=['DELETE'])
def projects_delete(id):
    return {"projects_delete": f"{id}"}


@main_bp.route('/projects/<number>/interfaces/', methods=['GET'])
@jwt_required
def projects_interfaces(number):
    # 获取用户信息
    username = get_jwt_identity()
    # print(username)
    # user = User.query.filter_by(username=username).first()

    # ------ 手工处理接收的数据 ------
    """
    projects = Projects.query.all()

    # 序列化 projects ==> json
    return {"projects_interfaces": [project.interfaces for project in projects]}   
    """

    project = Projects.query.get(number)
    interfaces = project.interfaces
    schema = se.InterfacesSchema(many=True, only=['id', 'name'])
    interfaces_json = schema.dump(interfaces)

    return jsonify(interfaces_json)


@main_bp.route('/projects/<id>/run/', methods=['POST'])
def projects_run(id):
    return {"projects_run": f"{id}"}


# ------ interfaces,需要pop project name（没有这个方法） ------

@main_bp.route('/interfaces/', methods=['GET'])
def interfaces_list():
    interfaces = Interfaces.query.all()
    schema = se.InterfacesSchema(many=True, exclude=['status', 'updated_at'])
    interfaces_json = schema.dump(interfaces)
    return {"results": interfaces_json}


@main_bp.route('/interfaces/', methods=['POST'])
def interfaces_create():
    """
    # ------ 手动获取数据进行处理 ------
    req_data = request.json
    # {"name": "", "tester": "", "programmer": ""}
    interface = Interfaces(**req_data)
    # 把你要提交的需要存储的数据放到 session
    # db.session.add(project)
    # # 提交事务
    # db.session.commit()
    interface.save()
    return {'result': interface.name}
    """

    # 从客户端接收数据
    req_data = request.json
    # 初始化序列化器
    schema = se.InterfacesSchema()
    # 反序列化, 还是一个字典（校验的过程）
    interface = schema.load(req_data)

    # project_info = interface.pop("project")
    # interface.setdefault("project_id", project_info["pid"])
    # # AttributeError: 'Interfaces' object has no attribute 'pop'

    # 序列化输出
    schema_out = se.InterfacesSchema(exclude=['status', 'updated_at'])
    interfaces_json = schema_out.dump(interface)
    return interfaces_json


@main_bp.route('/interfaces/names/', methods=['GET'])
def interfaces_names():
    return {"result": "interfaces_names"}


@main_bp.route('/interfaces/<id>/', methods=['GET'])
def interfaces_read(id):
    interface = Interfaces.query.get(id)
    schema = se.InterfacesSchema(exclude=['status', 'updated_at'])
    interface_json = schema.dump(interface)

    return jsonify(interface_json)


@main_bp.route('/interfaces/<id>/', methods=['PUT'])
def interfaces_update(id):
    return {"interfaces_update": f"{id}"}


@main_bp.route('/interfaces/<id>/', methods=['PATCH'])
def interfaces_partial_update(id):
    return {"interfaces_partial_update": f"{id}"}


@main_bp.route('/interfaces/<id>/', methods=['DELETE'])
def interfaces_delete(id):
    return {"interfaces_delete": f"{id}"}


@main_bp.route('/interfaces/<id>/configs/', methods=['GET'])
def interfaces_configs(id):
    interface = Interfaces.query.get(id)
    configs = interface.configs
    schema = se.ConfiguresSchema(many=True, only=['id', 'name'])
    Configs_json = schema.dump(configs)

    return jsonify(Configs_json)


@main_bp.route('/interfaces/<id>/run/', methods=['POST'])
def interfaces_run(id):
    return {"interfaces_run": f"{id}"}


@main_bp.route('/interfaces/<id>/testcases/', methods=['GET'])
def interfaces_testcases(id):
    return {"interfaces_testcases": f"{id}"}


# ------ configures ------

@main_bp.route('/configures/', methods=['GET'])
def configures_list():
    return {"result": "configures_list"}


@main_bp.route('/configures/', methods=['POST'])
def configures_create():
    # 创建 Project 对象，保存
    # 生成 Project

    req_data = request.json
    # {"name": "", "tester": "", "programmer": ""}
    configures = Configures(**req_data)
    # 把你要提交的需要存储的数据放到 session
    # db.session.add(project)
    # # 提交事务
    # db.session.commit()
    configures.save()
    return {'result': 1}
    # return {"result": "projects_create"}


@main_bp.route('/configures/<id>/', methods=['GET'])
def configures_read(id):
    return {"configures_read": f"{id}"}


@main_bp.route('/configures/<id>/', methods=['PUT'])
def configures_update(id):
    return {"configures_update": f"{id}"}


@main_bp.route('/configures/<id>/', methods=['PATCH'])
def configures_partial_update(id):
    return {"configures_partial_update": f"{id}"}


@main_bp.route('/interfaces/<id>/', methods=['DELETE'])
def configures_delete(id):
    return {"configures_delete": f"{id}"}


# ------ debugtalks ------

@main_bp.route('/debugtalks/', methods=['GET'])
def debugtalks_list():
    return {"result": "debugtalks_list"}


@main_bp.route('/debugtalks/<id>/', methods=['GET'])
def debugtalks_read(id):
    return {"debugtalks_read": f"{id}"}


@main_bp.route('/debugtalks/<id>/', methods=['PUT'])
def debugtalks_update(id):
    return {"debugtalks_update": f"{id}"}


@main_bp.route('/debugtalks/<id>/', methods=['PATCH'])
def debugtalks_partial_update(id):
    return {"debugtalks_partial_update": f"{id}"}


# ------ reports ------

@main_bp.route('/reports/', methods=['GET'])
def reports_list():
    return {"result": "reports_list"}


@main_bp.route('/reports/<id>/', methods=['GET'])
def reports_read(id):
    return {"reports_read": f"{id}"}


@main_bp.route('/reports/<id>/', methods=['DELETE'])
def reports_delete(id):
    return {"reports_delete": f"{id}"}


@main_bp.route('/reports/<id>/download/', methods=['GET'])
def reports_download(id):
    return {"reports_download": f"{id}"}


# ------ summary ------

@main_bp.route('/summary/', methods=['GET'])
def summary_list():
    return {"result": "summary_list"}


# ------ testcases ------

@main_bp.route('/testcases/', methods=['GET'])
def testcases_list():
    testcases = Testcases.query.all()
    schema = se.TestcasesSchema(many=True, exclude=['status', 'updated_at'])
    testcases_json = schema.dump(testcases)
    return {"results": testcases_json}


@main_bp.route('/testcases/', methods=['POST'])
def testcases_create():
    """
    # ------ 手动获取数据进行处理 ------
    req_data = request.json
    # {"name": "", "tester": "", "programmer": ""}
    testcases = Testcases(**req_data)
    # 把你要提交的需要存储的数据放到 session
    # db.session.add(project)
    # # 提交事务
    # db.session.commit()
    testcases.save()
    return {'result': 1}
    # return {"result": "projects_create"}
    """

    # 从客户端接收数据
    req_data = request.json

    # 获取interface_id
    interface_info = req_data.pop("interface")
    req_data.setdefault('interface_id', interface_info['iid'])
    
    # 初始化序列化器
    schema = se.TestcasesSchema()
    # 反序列化, 还是一个字典（校验的过程）
    testcase = schema.load(req_data)

    # 序列化输出
    schema_out = se.TestcasesSchema(exclude=['status', 'updated_at'])
    testcase_json = schema_out.dump(testcase)
    return testcase_json


@main_bp.route('/testcases/<id>/', methods=['GET'])
def testcases_read(id):
    return {"testcases_read": f"{id}"}


@main_bp.route('/testcases/<id>/', methods=['PUT'])
def testcases_update(id):
    return {"testcases_update": f"{id}"}


@main_bp.route('/testcases/<id>/', methods=['PATCH'])
def testcases_partial_update(id):
    return {"testcases_partial_update": f"{id}"}


@main_bp.route('/testcases/<id>/', methods=['DELETE'])
def testcases_delete(id):
    return {"testcases_delete": f"{id}"}


@main_bp.route('/testcases/<id>/run/', methods=['POST'])
def testcases_run(id):
    return {"testcases_run": f"{id}"}


# ------ testsuits ------

@main_bp.route('/testsuits/', methods=['GET'])
def testsuits_list():
    return {"result": "testsuits_list"}


@main_bp.route('/testsuits/', methods=['POST'])
def testsuits_create():
    # 创建 Project 对象，保存
    # 生成 Project

    req_data = request.json
    # {"name": "", "tester": "", "programmer": ""}
    testsuits = Testsuits(**req_data)
    # 把你要提交的需要存储的数据放到 session
    # db.session.add(project)
    # # 提交事务
    # db.session.commit()
    testsuits.save()
    return {'result': 1}
    # return {"result": "projects_create"}


@main_bp.route('/testsuits/<id>/', methods=['GET'])
def testsuits_read(id):
    return {"testsuits_read": f"{id}"}


@main_bp.route('/testsuits/<id>/', methods=['PUT'])
def testsuits_update(id):
    return {"testsuits_update": f"{id}"}


@main_bp.route('/testsuits/<id>/', methods=['PATCH'])
def testsuits_partial_update(id):
    return {"testsuits_partial_update": f"{id}"}


@main_bp.route('/testsuits/<id>/', methods=['DELETE'])
def testsuits_delete(id):
    return {"testsuits_delete": f"{id}"}


@main_bp.route('/testsuits/<id>/run/', methods=['POST'])
def testsuits_run(id):
    return {"testsuits_run": f"{id}"}


