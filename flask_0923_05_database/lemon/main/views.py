# -*- coding: UTF-8 -*-
# 当前项目的名称: flask_class 
# 新文件名称：views 
# 当前登录名：LuckyLu
# 创建日期：2020/9/24 10:42
# 文件IDE名称：PyCharm

from flask import request
from flask.views import MethodView


from lemon.main.bluerpint import main_bp
from lemon.main.models import Projects, Interfaces, Configures, DebugTalks, Envs, Reports, Summary, Testcases, Testsuits

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
@main_bp.route('/projects/', methods=['GET'])
def projects_list():
    return {"result": "project_list"}


@main_bp.route('/projects/', methods=['POST'])
def projects_create():
    # 创建 Project 对象，保存
    # 生成 Project

    req_data = request.json
    # {"name": "", "tester": "", "programmer": ""}
    project = Projects(**req_data)
    # 把你要提交的需要存储的数据放到 session
    # db.session.add(project)
    # # 提交事务
    # db.session.commit()
    project.save()
    return {'result': 1}
    # return {"result": "projects_create"}


@main_bp.route('/projects/names/', methods=['GET'])
def projects_names():
    return {"result": "projects_names"}


@main_bp.route('/projects/<id>/', methods=['GET'])
def projects_read(id):
    return {"projects_read": f"{id}"}


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
def projects_interfaces(number):
    return {"projects_interfaces": f"{number}"}


@main_bp.route('/projects/<id>/run/', methods=['POST'])
def projects_run(id):
    return {"projects_run": f"{id}"}


# ------ interfaces ------

@main_bp.route('/interfaces/', methods=['GET'])
def interfaces_list():
    return {"result": "interfaces_list"}


@main_bp.route('/interfaces/', methods=['POST'])
def interfaces_create():
    # 创建 Project 对象，保存
    # 生成 Project

    req_data = request.json
    # {"name": "", "tester": "", "programmer": ""}
    interface = Interfaces(**req_data)
    # 把你要提交的需要存储的数据放到 session
    # db.session.add(project)
    # # 提交事务
    # db.session.commit()
    interface.save()
    return {'result': 1}
    # return {"result": "projects_create"}


@main_bp.route('/interfaces/names/', methods=['GET'])
def interfaces_names():
    return {"result": "interfaces_names"}


@main_bp.route('/interfaces/<id>/', methods=['GET'])
def interfaces_read(id):
    return {"interfaces_read": f"{id}"}


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
    return {"interfaces_configs": f"{id}"}


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


# ------ envs ------

@main_bp.route('/envs/', methods=['GET'])
def envs_list():
    return {"result": "envs_list"}


@main_bp.route('/envs/', methods=['POST'])
def envs_create():
    # 创建 Project 对象，保存
    # 生成 Project

    req_data = request.json
    # {"name": "", "tester": "", "programmer": ""}
    envs = Envs(**req_data)
    # 把你要提交的需要存储的数据放到 session
    # db.session.add(project)
    # # 提交事务
    # db.session.commit()
    envs.save()
    return {'result': 1}
    # return {"result": "projects_create"}


@main_bp.route('/envs/names/', methods=['GET'])
def envs_names():
    return {"result": "envs_names"}


@main_bp.route('/envs/<id>/', methods=['GET'])
def envs_read(id):
    return {"envs_read": f"{id}"}


@main_bp.route('/envs/<id>/', methods=['PUT'])
def envs_update(id):
    return {"envs_update": f"{id}"}


@main_bp.route('/envs/<id>/', methods=['PATCH'])
def envs_partial_update(id):
    return {"envs_partial_update": f"{id}"}


@main_bp.route('/envs/<id>/', methods=['DELETE'])
def envs_delete(id):
    return {"envs_delete": f"{id}"}


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
    return {"result": "testcases_list"}


@main_bp.route('/testcases/', methods=['POST'])
def testcases_create():
    # 创建 Project 对象，保存
    # 生成 Project

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


