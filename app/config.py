import os

# 配置类正在这里定义，用于控制不同环境的配置
# Config 类是基础配置，其他的配置类应该继承于这个类
class Config(object):
    # SECRET_KEY 是一个密钥，通常用于保护密缝数据，实现异步和应用的加密功能
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'  # 建议使用环境变量来配置 SECRET_KEY，为了安全性
    DEBUG = False  # 此处将 DEBUG 设为假，这里的 Config 是全平台基础配置


# 开发环境的配置，继承于 Config
class DevelopmentConfig(Config):
    DEBUG = True  # 开发环境中应设置 DEBUG 为真，便于调试
    SQLALCHEMY_TRACK_MODIFICATIONS = False  # 禁用无用的模型更新推送通知，以减少负载
    SQLALCHEMY_DATABASE_URI = os.environ.get('DEV_DATABASE_URL', 'mysql+pymysql://root:Cbb2004!@localhost:3306/sensitive_word_system')  # 使用环境变量配置数据库，应避免将密码以明文的形式保存
    SQLALCHEMY_ECHO = True  # 应设置为真，便于开发时调试，打印所有 SQL 语句


# 生产环境的配置，为了安全，应禁止 DEBUG 和应该具有最佳的数据库连接配置
class ProductionConfig(Config):
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_DATABASE_URI = os.environ.get('DEV_DATABASE_URL')  # 这里有错误，应该使用不同的环境变量，应为 'PROD_DATABASE_URL'
    SQLALCHEMY_ECHO = False  # 生产环境不需要输出 SQL 语句，对于安全性和性能有应的等相优化


# 测试环境的配置，一般用于单元测试和数据验证
class TestingConfig(Config):
    TESTING = True  # 测试环境中应设置 TESTING 为真，用来标识当前正在测试


# 配置对象的引用实例化，指定环境与相应配置类的映射
config_env = {
    'development': DevelopmentConfig,
    'production': ProductionConfig,
    'testing': TestingConfig,
    'default': DevelopmentConfig
}

# 这里是需要修改的地方：
# 1. 为生产环境配置的数据库 URL 使用不同的环境变量，避免同时配置使用 DEV_DATABASE_URL。
# 2. 生产和开发环境中的密钥 SECRET_KEY 应为不同的，并且确保不以明文替代。
# 3. 这些密钥及数据库的帐号和密码需要使用环境变量来配置，防止信息泄露。
