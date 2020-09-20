import time
from datetime import datetime

from flask import Flask, render_template, redirect

app = Flask(
    __name__,
    template_folder='pages',
    static_folder='static'
)


def log_time(f):
    def decorator():
        print(time.time())
        return f()
    return decorator


@app.route('/')
@log_time
def project():
    return "project"


if __name__ == '__main__':
    app.run(debug=True)