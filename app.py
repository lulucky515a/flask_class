from datetime import datetime

from flask import Flask, request, redirect, render_template

app = Flask(__name__)

# 修改配置
app.config['JSON_AS_ASCII'] = False


@app.route('/', methods=['POST'])
def hello_world():
    # 获取 请求当中 post， 数据
    body_data = request.form
    # body_data = request.json
    print(body_data)
    print(body_data['username'])
    return """
    <html>
        <p style="color:red"> hello world路上发士大夫</p>
    </html>
    """


@app.route('/project')
def project():
    # 定制响应状态码和 header
    return {"msg": "欢迎光临"}, 201, {"hello": "world"}

    # 重定向
    # return redirect('/')

# 模板渲染
@app.route('/projects')
def projects():
    # 渲染 HTML 文件

    projects = [
        {"name": "project01", "tester": "yuz", "created_at": datetime.now()},
        {"name": "project02", "tester": "musen", "created_at": datetime.now()},
    ]
    print(app.config)
    print(request.headers)

    return render_template('index.html', p=projects)

# 注册filter
@app.template_filter()
def dt_to_str(dt):
    return dt.strftime('%Y/%m/%d')

# 注册 test
@app.template_test()
def is_yuz(data):
    if data == 'yuz':
        return True
    return False


# @app.template_global

if __name__ == '__main__':
    app.run(debug=True)
    

