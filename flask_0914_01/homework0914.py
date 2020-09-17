# -*- coding: UTF-8 -*-
# 当前项目的名称: ORMWork 
# 新文件名称：homework0914 
# 当前登录名：LuckyLu
# 创建日期：2020/9/15 15:43
# 文件IDE名称：PyCharm

"""
wsgi作业
截至：09月17日  17:59展示词云
通过 python 的 wsgi server 实现一个简易框架，具备以下功能：


1、定义 3 个 url 。 '/' 首页， '/login' 登录 '/projects' 项目
2、对三个 url 做出对应的响应，繁简由人。
3、如果访问不在指定的 3 个 url, 报 404 错误.
"""

from flask import Flask, request

# 得到 app 对象
app = Flask(__name__)


# 路由
@app.route('/login/')
def index():
    return "login success"


@app.route('/')
def home():
    return "welcome this is homepage!"


@app.route('/projects/')
def project_one():
    # id = request.args.get("id")
    # print(id)
    # return str(id)
    return "projects"


app.run(debug=True)