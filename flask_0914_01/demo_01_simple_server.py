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


# def app(env, response):
#     """flask / django application"""
#     print("正在监听")
#     response('200 OK', [("content-type", 'text/html')])
#     if env['PATH_INFO'] == '/login/':
#         return [b'login success']
#     elif env['PATH_INFO'] == '/projects/':
#         return [b'projects']
#     else:
#         return [b'not found this page']


def app(env, response):
    """flask / django application"""
    print("正在监听")
    response('200 OK', [("content-type", 'text/html')])
    # url_map['/login/'] ==> login
    return url_map.get(env['PATH_INFO'])()


# 初始化一个服务器
server = make_server('', 5100, app)
server.serve_forever(0.2)
