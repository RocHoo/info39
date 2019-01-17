from redis import StrictRedis



class Config():
    DEBUG=None

    SECRET_KEY='u52oD3HifrG9m6vE0q+rbKNqk7l++v6u+256wmjh744GPEJQRLnmkA=='

    SQLALCHEMY_DATABASE_URI='mysql://root:mysql@localhost/info_python37'

    SQLALCHEMY_TRACK_MODIFICATIONS=False

    SESSION_TYPE='redis'

    SESSION_USER_SINGER=True

    SESSION_REDIS=StrictRedis(host='127.0.0.1',port=6379)

    PERMANENT_SESSION_LIFETIME=64800

class DevelopmentConfig(Config):
    DEBUG=True

class ProductionConfig(Config):
    DEBUG=False

config_dict={
    'development':DevelopmentConfig,
    'production':ProductionConfig
}