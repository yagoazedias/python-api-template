from os import getenv


class Config(object):
    DEBUG = False
    TESTING = False


class ProductionConfig(Config):
    DEBUG = False
    TESTING = False
    PORT = getenv('PORT')


class PreProductionConfig(Config):
    DEBUG = False
    TESTING = False
    PORT = 2000


class DevelopmentConfig(Config):
    DEBUG = True
    TESTING = True
    PORT = 3000
