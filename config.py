import os

basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY')

    BLOB_ACCOUNT = os.environ.get('BLOB_ACCOUNT')
    BLOB_STORAGE_KEY = os.environ.get('BLOB_STORAGE_KEY')
    BLOB_CONTAINER = os.environ.get('BLOB_CONTAINER')

    SQL_SERVER = os.environ.get('SQL_SERVER')
    SQL_DATABASE = os.environ.get('SQL_DATABASE')
    SQL_USER_NAME = os.environ.get('SQL_USER_NAME')
    SQL_PASSWORD = os.environ.get('SQL_PASSWORD')
    SQLALCHEMY_DATABASE_URI = (
        'mssql+pyodbc://{username}:{password}@{server}:1433/{database}'
        '?driver=ODBC+Driver+18+for+SQL+Server&Encrypt=yes&TrustServerCertificate=no&Connection+Timeout=30'
        .format(
            username=os.environ.get('SQL_USER_NAME'),
            password=os.environ.get('SQL_PASSWORD'),
            server=os.environ.get('SQL_SERVER'),
            database=os.environ.get('SQL_DATABASE')
        )
    )

    SQLALCHEMY_TRACK_MODIFICATIONS = False

    CLIENT_SECRET = os.environ.get('CLIENT_SECRET')
    AUTHORITY = "https://login.microsoftonline.com/common"
    CLIENT_ID = os.environ.get('CLIENT_ID')
    REDIRECT_PATH = "/getAToken"
    SCOPE = ["User.Read"]
    SESSION_TYPE = "filesystem"
