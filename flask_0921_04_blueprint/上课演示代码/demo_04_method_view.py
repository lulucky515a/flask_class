# methodview: flask 针对现在的 RESTful 风格的接口设计出来，
# View 类衍生出来的现成写法。
# get, post 方法，就可以直接用了， 不需要写 dispatch_request
# get: 获取资源
# post: 创建资源
# put: 更新资源
# delete: 删除资源
# /project

from flask import Flask, request
from flask.views import View, MethodView

app = Flask(
    __name__,
    template_folder='pages',
    static_folder='static'
)


class ProjectView(MethodView):
    # 实现指定的 methods 类属性，照样可以控制请求方法。
    # 就算类当中实现了 实例方法 get, post, 也是不支持对应的请求方法的。
    methods = ['GET']

    def get(self):
        """get"""
        return "method get project"

    def post(self):
        return "method post project"

    def put(self):
        return "method put project"


# 注册视图
# 基于类的视图，不要用装饰器，采取集中注册的形式，add_url_rule
# TODO: PR
app.add_url_rule('/project', view_func=ProjectView.as_view('project'))

if __name__ == '__main__':
    app.run(debug=True)