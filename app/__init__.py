from config import config
from flask import Flask


def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config[config_name])
    # 注册蓝图
    from app.api_1_0 import bp
    app.register_blueprint(bp)

    return app
