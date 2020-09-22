# methodview: flask 针对现在的 RESTful 风格的接口设计出来，
# View 类衍生出来的现成写法。
# get, post 方法，就可以直接用了， 不需要写 dispatch_request
# get: 获取资源
# post: 创建资源
# put: 更新资源
# delete: 删除资源
# /project

from flask import Flask, request
from flask.views import View

app = Flask(
    __name__,
    template_folder='pages',
    static_folder='static'
)


class MethodView(View):
    methods = ['get', 'post', 'put', 'delete']

    def dispatch_request(self):
        """一定要实现，这是一个规范。
        第二次请求的分派
        """
        # 获取请求方法，根据请求方法，调用不同的实例方法
        # 请求：判断 content-type: json, form, xml
        # 请求：能不能在获取客户端的IP, 限流。
        def dispatch_request(self):
            method = request.method.lower()
            view_func = getattr(self, method, '')
            if (method in self.methods) and view_func:
                return view_func()
            else:
                return {"msg": 'method not allowd'}


class ProjectView(MethodView):
    def get(self):
        print("myself get project")


# 注册视图
# 基于类的视图，不要用装饰器，采取集中注册的形式，add_url_rule
# TODO: PR
app.add_url_rule('/project', view_func=ProjectView.as_view('project'))

if __name__ == '__main__':
    app.run(debug=True)