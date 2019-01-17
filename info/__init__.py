from flask import Flask
# 导入扩展flask_session
from flask_session import Session
# 导入sqlalchemy扩展
from flask_sqlalchemy import SQLAlchemy
# 导入配置对象
from config import config_dict, Config

from redis import StrictRedis
import logging
from logging.handlers import RotatingFileHandler

# 实例化sqlalchemy对象
db = SQLAlchemy()

redis_store = StrictRedis(host=Config.REDIS_HOST, port=Config.REDIS_PORT,password='mysql')





# 定义工厂函数，封装创建程序实例的代码；
# 作用：可以给函数传入参数，动态的决定，以什么模式下运行代码,

def create_app(config_name):
    app = Flask(__name__)
    # 使用抽取出去的配置信息
    app.config.from_object(config_dict[config_name])

    # 让Session扩展和程序实例进行关联
    Session(app)
    # 通过函数，实现db和app的关联
    db.init_app(app)

    # 导入蓝图
    from info.modules.news import news_blue
    app.register_blueprint(news_blue)
    from info.modules.passport import passport_blue
    app.register_blueprint(passport_blue)
    logging.basicConfig(level=logging.DEBUG)

    file_log_handler = RotatingFileHandler('logs/log', maxBytes=1024 * 1024 * 100, backupCount=10)

    formatter = logging.Formatter('%(levelname)s %(filename)s:%(lineno)d %(message)s')

    file_log_handler.setFormatter(formatter)

    logging.getLogger().addHandler(file_log_handler)
    return app
