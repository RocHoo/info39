from redis import StrictRedis


class Config():
    DEBUG = None

    SECRET_KEY = 'u52oD3HifrG9m6vE0q+rbKNqk7l++v6u+256wmjh744GPEJQRLnmkA=='

    SQLALCHEMY_DATABASE_URI = 'mysql://root:mysql@localhost/info_python37'

    SQLALCHEMY_TRACK_MODIFICATIONS = False

    SESSION_TYPE = 'redis'

    SESSION_USER_SINGER = True

    REDIS_HOST = '127.0.0.1'

    REDIS_PORT = 6379

    SESSION_REDIS = StrictRedis(password='mysql',host=REDIS_HOST, port=REDIS_PORT)

    PERMANENT_SESSION_LIFETIME = 64800


class DevelopmentConfig(Config):
    DEBUG = True


class ProductionConfig(Config):
    DEBUG = False


config_dict = {'development': DevelopmentConfig, 'production': ProductionConfig}
