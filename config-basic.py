import os
import random, string

class Config(object):
    CSRF_ENABLED = True
    SECRET = 'CRIE UMA CHAVE SECRETA E ADICIONE AQUI - 64BITS É O RECOMENDADO'
    TEMPLATE_FOLDER = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'templates')
    ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
    APP = None
    DB = None
    MONGO = None

class DevelopmentConfig(Config):
    TESTING = False
    DEBUG = True
    IP_HOST = 'localhost'
    PORT_HOST = 8000
    URL_MAIN = 'http://%s:%s/' % (IP_HOST, PORT_HOST)

    MONGO_HOST = "127.0.0.1"
    MONGO_PORT = 27017
    MONGO_DBNAME = "starWars"
    MONGO_USERNAME = ""
    MONGO_PASSWORD = ""

class TestingConfig(Config):
    TESTING = True
    DEBUG = True
    IP_HOST = 'localhost' # Aqui geralmente é um IP de um servidor na nuvem e não o endereço da máquina local
    PORT_HOST = 5000
    URL_MAIN = 'http://%s:%s/' % (IP_HOST, PORT_HOST)

    MONGO_HOST = "127.0.0.1"
    MONGO_PORT = 27017
    MONGO_DBNAME = "starWars"
    MONGO_USERNAME = ""
    MONGO_PASSWORD = ""

class ProductionConfig(Config):
    DEBUG = False
    TESTING = False
    IP_HOST = '0.0.0.0' # Aqui geralmente é um IP de um servidor na nuvem e não o endereço da máquina local
    PORT_HOST = 5000
    URL_MAIN = 'http://%s:%s/' % (IP_HOST, PORT_HOST)

    MONGO_HOST = "127.0.0.1"
    MONGO_PORT = 27017
    MONGO_DBNAME = "starWars"
    MONGO_USERNAME = ""
    MONGO_PASSWORD = ""

app_config = {
    'development': DevelopmentConfig(),
    'testing': TestingConfig(),
    'production': ProductionConfig()
}

app_active = os.getenv('FLASK_ENV')
if app_active is None:
    app_active = 'development'
