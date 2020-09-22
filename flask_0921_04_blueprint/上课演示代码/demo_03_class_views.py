# 类视图
# 1，flask 之前是没有类视图，可插拔视图
# 2，从 django 借鉴。

from flask import Flask, request
from flask.views import View

app = Flask(
    __name__,
    template_folder='pages',
    static_folder='static'
)


class ProjectView(View):

    # View 视图一定要记得定义 methods
    methods = ['GET', 'POST', 'PUT']

    def get(self):
        """get"""
        return "get project"

    def post(self):
        return "post project"

    def dispatch_request(self):
        """一定要实现，这是一个规范。
        第二次请求的分派
        """
        # 获取请求方法，根据请求方法，调用不同的实例方法
        # 请求：判断 content-type: json, form, xml
        # 请求：能不能在获取客户端的IP, 限流。
        method = request.method.lower()
        if method == 'get':
            return self.get()
        elif method == 'post':
            return self.post()

        return "method not allowed", 405


# 注册视图
# 基于类的视图，不要用装饰器，采取集中注册的形式，add_url_rule
# TODO: PR
app.add_url_rule('/project', view_func=ProjectView.as_view('project'))


# 之所以类视图能够生效，是因为类实现了 as_view 这个方法
# 视图函数， /project ==> def project()
# 类视图： /project ==> def view()  ==> dispatch_request()


if __name__ == '__main__':
    app.run(debug=True)