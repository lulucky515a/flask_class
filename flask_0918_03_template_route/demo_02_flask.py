from datetime import datetime

from flask import Flask, render_template, redirect

app = Flask(
    __name__,
    template_folder='pages',
    static_folder='static'
)


@app.route('/login')
def login():
    return "login"

app.add_url_rule('/login', login)
print(app.url_map)


if __name__ == '__main__':
    app.run(debug=True)