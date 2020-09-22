from flask import Flask, render_template, redirect

app = Flask(
    __name__,
    template_folder='pages',
    static_folder='static'
)

# 问题1：一个URL --> 多个视图函数
# 问题2：一个视图函数 --》 多个URL
# project
# login
# @app.route('/project', methods=['GET'])
# def projects():
#     return "projects"
#
# @app.route('/project', methods=['POST'])
# def login():
#     return "login"


@app.route('/project')
@app.route('/login')
def login():
    return "login"


if __name__ == '__main__':
    app.run(debug=True)