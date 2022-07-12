DIALECT = 'mysql'
DRIVER = 'pymysql'
USERNAME = 'root'
PASSWORD = '123456'
HOST = '192.168.2.80'
PORT = '3306'
DATABASE = 'demo'

SQLALCHEMY_DATABASE_URI = "{}+{}://{}:{}@{}:{}/{}?charset=utf8".format(DIALECT, DRIVER, USERNAME, PASSWORD, HOST, PORT,
                                                                       DATABASE)
SQLALCHEMY_TRACK_MODIFICATIONS = False
SQLALCHEMY_POOL_SIZE = 5
SQLALCHEMY_ECHO = True

SIGN_SECRET_KEY  = "SECRET_KEY"
TOKEN_SECRET_KEY = "SECRET_KEY"
