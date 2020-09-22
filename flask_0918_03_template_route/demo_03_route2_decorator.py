# URL 和 视图函数的绑定


# 当用户输入某个字符串时， 就能调用某个对应的函数
from wsgiref.simple_server import make_server

url_map = {}

def add_url_rule(url, view_func):
    """添加路由，"""
    url_map[url] = view_func
    # 可以使用url_map.setdefault()设置默认值
    # 当url（key）存在就不会设置，如果不存在使用url设置
    # url_map.setdefault(url, view_func)

def route(url):
    """路由装饰器"""
    def decorator(f):
        add_url_rule(url, f)
        return f
    return decorator


@route('/login')
def login():
    return "login"


@route('/project')
def projects():
    return "projects"


print(url_map)


def app(env, start_response):
    url = env.get('PATH_INFO')  # 接口地址
    # parame = env.get('QUERY_STRING')
    if url is None or (url not in url_map.keys()):
        start_response('404 ok', [('content-type', 'text/plain'), ])
        res = '页面不存在'
        return [res.encode()]

    else:
        start_response('200 ok', [('content-type', 'text/plain'), ])
        res = url_map.get(url)
        print(res)
        return [res().encode()]



if __name__ == '__main__':
    server = make_server("", 6005, app)  # 创建一个服务

    server.serve_forever()  # 开启一个服务
