from datetime import datetime

from flask import Flask, render_template, redirect

app = Flask(
    __name__,
    template_folder='pages',
    static_folder='static'
)


@app.route('/')
def index():
    projects = [
        {"name": "project01", "tester": "yuz", "created_at": datetime.now()},
        {"name": "project02", "tester": "musen", "created_at": datetime.now()},
    ]
    return render_template('index.html', projects=projects)


@app.route('/login/')
def login():
    return render_template('login.html')


@app.route('/login_handler', methods=['POST'])
def login_handler():
    # 检验
    return redirect('/')



if __name__ == '__main__':
    app.run(debug=True)