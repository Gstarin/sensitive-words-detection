from flask import Flask

from .config import config_env
from .extensions import db, bootstrap


def create_app(config_name="default"):
    app = Flask(__name__)
    app.config.from_object(config_env[config_name])
    # 扩展
    db.init_app(app)
    bootstrap.init_app(app)
    # 蓝图注册
    from .admin import admin_bp
    app.register_blueprint(admin_bp)
    from .main import main_bp
    app.register_blueprint(main_bp)
    return app
