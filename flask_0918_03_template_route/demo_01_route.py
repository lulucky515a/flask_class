# URL 和 视图函数的绑定


# 当用户输入某个字符串时， 就能调用某个对应的函数

def login():
    return "login"

def projects():
    return "projects"

url_map = {}

def add_url_rule(url, view_func):
    """添加路由，"""
    url_map[url] = view_func

add_url_rule('/login', view_func=login)
add_url_rule('/project', view_func=login)

print(url_map)

if __name__ == '__main__':
    while True:
        url = input("请输入url")
        print(url_map[url]())