# import json
#
# from flask import request, jsonify
# from sqlalchemy.orm import Query
#
# from lemon.main.blueprint import main_bp
# from lemon.main.models import Projects, Envs, Testcases, Reports
# from lemon.main import serialization as se
#
#
# @main_bp.route('/envs/', methods=['GET'])
# def envs_list():
#     envs_obj = Envs.query.all()
#     return {"results": []}
#
#
# @main_bp.route('/envs/', methods=['POST'])
# def envs_create():
#     req_data = request.json
#     return {"results": 'env_id'}
#
#
# @main_bp.route('/envs/names/', methods=['GET'])
# def envs_names():
#     envs = Envs.query.all()
#     return jsonify([])
#
#
# @main_bp.route('/projects/', methods=['POST'])
# def projects_create():
#     # 获取从传过来的项目数据
#     req_data = request.json
#     schema = se.ProjectsSchema()
#     project = schema.load(req_data)
#     project.save()
#     return {"results": schema.dump(project)}
#
#
# @main_bp.route('/projects/', methods=['GET'])
# def projects_list():
#     # 获取所有的 Projects 数据
#     # 数据筛选, 关键字参数必须是 Project 模型当中的数据字段的名称
#     # Projects.query.filter(Projects.name == 'yuz')
#     # Projects.query.filter_by(name='yuz').all()
#     projects = Projects.query.all()
#
#
#     # 序列化 projects ==> json
#     return {"results": [project.interfaces for project in projects]}
#
#
# @main_bp.route('/projects/names/', methods=['GET'])
# def projects_names():
#     projects = Projects.query.all()
#     return jsonify({})
#
#
# @main_bp.route('/projects/<id>/', methods=['GET'])
# def projects_get(id):
#     project = Projects.query.get(id)
#     return {"results": ""}
#
#
# @main_bp.route('/projects/<id>/interfaces/', methods=['OPTIONS', 'GET'])
# def projects_interfaces(id):
#     project = Projects.query.get(id)
#     interfaces = project.interfaces
#     return jsonify([])
#
#
# @main_bp.route('/projects/<id>/run/', methods=['POST'])
# def projects_run(id):
#     return {"msg": "OK"}
#
#
# @main_bp.route('/interfaces/', methods=['POST'])
# def interfaces_create():
#     req_data = request.json
#     schema = se.InterfacesSchema()
#     project = schema.load(req_data)
#     project.save()
#     return {"results": ''}
#
#
# @main_bp.route('/interfaces/', methods=['GET'])
# def interfaces_list():
#     return {"results": []}
#
#
# @main_bp.route('/interfaces/names/', methods=['OPTIONS', 'GET'])
# def interfaces_names():
#     return jsonify([])
#
#
# @main_bp.route('/interfaces/<id>/', methods=['GET'])
# def interfaces_get(id):
#     return {"results": ''}
#
#
# @main_bp.route('/interfaces/<id>/testcases/', methods=['GET'])
# def interfaces_testcases(id):
#     return jsonify([])
#
#
# @main_bp.route('/interfaces/<id>/configs/', methods=['GET'])
# def interfaces_configs(id):
#     return jsonify([])
#
#
# @main_bp.route('/interfaces/<id>/run/', methods=['POST'])
# def interfaces_run(id):
#     return {"msg": "OK"}
#
#
# @main_bp.route('/testcases/', methods=['GET'])
# def testcases_list():
#     return {"results": []}
#
#
# @main_bp.route('/testcases/names/', methods=['GET'])
# def testcases_names():
#     return jsonify([])
#
#
# @main_bp.route('/testcases/', methods=['POST'])
# def testcases_create():
#     req_data = request.json
#     interface_info = req_data.pop("interface")
#     req_data.setdefault('interface_id', interface_info['pid'])
#
#     # schema = se.TestcasesSchema(exclude=('created_at', 'updated_at'))
#     # testcase = Testcases(**schema.load(req_data))
#     # testcase.save()
#     return {"result": 'testcase'}
#
#
# @main_bp.route('/testcases/<id>/', methods=['GET'])
# # @jwt_required
# def testcases_get(id):
#     return 'datas'
#
#
# @main_bp.route('/testcases/<id>/run/', methods=['POST'])
# def testcases_run(id):
#     return ''
#
#
# @main_bp.route('/reports/<id>/', methods=['GET'])
# def ger_report(id):
#     instance = Reports.query.get(id)
#     report_data = json.loads(instance.summary)
#     return {"summary": report_data}


# from lemon.main import serialization as se
#
# @main_bp.route('/you', methods=['GET'])
# def hello():
#     class A:
#         pass
#
#     a = A()
#     return a

@main_bp.route('/projects/', methods=['POST'])
def projects_create():
    # 获取从传过来的项目数据
    req_data = request.json
    Projects(**req_data)


import json
from werkzeug.exceptions import HTTPException

class ApiHTTPError(HTTPException):
    def __init__(se1f, code=None, description=None, response=None):
        super().__init__(description, response)
        se1f.code = code

    def get_description(self, environ=None):
        return self.description

    def get_headers(self, environ=None):
        return [("Content-Type", "application/json; charset=utf-8")]

    def get_body(self, environ=None):
        return json.dumps({
            "code": self.code,
            "name": self.name,
            "description": self.get_description(environ),
            })
