# 作为调试运行程序
# 在本地或者测试的时候， 去启动服务器

# 你得有一个 app = Flask()
from lemon import create_app
# from lemon import app

from lemon import config, config_pathlib


app = create_app(setting=config_pathlib.DevConfig)

print(app.url_map)
print(app.config)

if __name__ == '__main__':
    app.run(port=8000)
    # app.run(debug=config.Config.DEBUG)
    # app.run(debug=config_pathlib.Config.DEBUG)