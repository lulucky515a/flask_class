# -*- coding: UTF-8 -*-
# 当前项目的名称: ORMWork 
# 新文件名称：flask_test 
# 当前登录名：LuckyLu
# 创建日期：2020/9/15 9:56
# 文件IDE名称：PyCharm 

"""
wsgi作业
截至：09月17日  17:59展示词云
通过 python 的 wsgi server 实现一个简易框架，具备以下功能：


1、定义 3 个 url 。 '/' 首页， '/login' 登录 '/projects' 项目
2、对三个 url 做出对应的响应，繁简由人。
3、如果访问不在指定的 3 个 url, 报 404 错误.
"""


from flask import Flask

from wsgiref.simple_server import make_server


# 视图函数 view function
def login():
    return [b"login"]

def project():
    return [b'projects']


url_map = {
    '/login/': login,
    '/projects/': project
}

def listen(env, make_response):
    print("正在监听")
    make_response('200 OK', [(' content-type',' text/p1ain')])
    # return [b'he11o']
    # if env['PATH_INFO'] == '/login/':
    #     return [b'login success']
    # elif env['PATH_INFO'] == '/projects/':
    #     return [b'projects']
    # else:
    #     return [b'not found this page']
    return url_map.get(env['PATH_INFO'])()


server = make_server("", 5032, listen)
server.serve_forever(0.2)


