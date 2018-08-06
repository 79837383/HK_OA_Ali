import os

class Config():
    strSQLIP = "127.0.0.1"
    intSQLPort = 3306

    strDBUserName = "root"
    strDBPassword = "xing"
    strDBName = "test"

    basedir = os.path.abspath(os.path.dirname(__file__))

config = Config()