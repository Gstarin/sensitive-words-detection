from flask import Flask
from .config import config_env
from .extensions import db, bootstrap


def create_app(config_name="default"):
    # 创建Flask应用实例
    app = Flask(__name__)
    # 加载配置，根据传入的config_name选择不同环境的配置
    app.config.from_object(config_env[config_name])

    # 初始化扩展，将数据库和Bootstrap与应用绑定
    db.init_app(app)
    bootstrap.init_app(app)

    # 蓝图注册，模块化管理路由
    from .admin import admin_bp  # 你已有的蓝图
    from .main import main_bp  # 注册 main_bp 蓝图

    app.register_blueprint(admin_bp)  # 注册 admin 蓝图
    app.register_blueprint(main_bp)  # 注册 main 蓝图

    # 返回配置好的应用实例
    return app
