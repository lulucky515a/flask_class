# -*- coding: UTF-8 -*-
# 当前项目的名称: flask_class 
# 新文件名称：views 
# 当前登录名：LuckyLu
# 创建日期：2020/9/24 10:42
# 文件IDE名称：PyCharm


from flask.views import MethodView


from lemon.main.bluerpint import main_bp

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
    return {"result": "projects_create"}


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





