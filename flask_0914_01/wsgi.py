from flask import Flask, request

# 得到 app 对象
app = Flask(__name__)


# 路由
@app.route('/login/')
def index():
    return "login success"


# @app.route('/projects/', methods=['POST', 'GET', 'PUT'])
# def projects():
#     return "projects"

# # 请求的参数1：url path， url 路径
# @app.route('/projects/<id>/')
# def project_one(id):
#     return f"project{id}"

# 请求的参数2：query string
@app.route('/projects/')
def project_one():
    id = request.args.get("id")
    print(id)
    return str(id)

# body, json, form  request.value


# 启动web服务， gunicorn, 也可以用 uwsgi, flask 自带的测试服务器
# 在生产环境不要去使用
# debug 模式有两个好处：1，重启启动;2,显示错误信息
app.run(debug=True)


