# 作为调试运行程序
# 在本地或者测试的时候， 去启动服务器

# 你得有一个 app = Flask()
from lemon import create_app
# from lemon import app

from lemon import config

app = create_app()

print(app.url_map)
print(app.config)

if __name__ == '__main__':
    # app.run(debug=True)
    app.run(debug=config.DevConfig)