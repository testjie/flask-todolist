import os
basedir = os.path.abspath(os.path.dirname(__file__))




class DevelopConfig:
    # PYMYSQL数据库的配置变量
    HOSTNAME = '192.168.1.88'
    PORT     = '3306'
    DATABASE = 'flask_todolist'
    USERNAME = 'root'
    PASSWORD = '123456'
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://{}:{}@{}:{}/{}'.format(USERNAME,PASSWORD,HOSTNAME,PORT,DATABASE)

    SQLALCHEMY_TRACK_MODIFICATIONS = True

    # FLASK启动配置
    DEBUG = True
    HOST = "0.0.0.0"

    # SESSION配置
    SECRET_KEY = os.urandom(24)



config = {
    "DevelopConfig":DevelopConfig
}