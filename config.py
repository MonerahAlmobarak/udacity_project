import os

class Config(object):
    # Flask Secret Key
    SECRET_KEY = os.environ.get('SECRET_KEY') or '3b7d!@Ud4c1tyCMS#2025'

    # Azure Blob Storage
    BLOB_ACCOUNT = os.environ.get('BLOB_ACCOUNT') or 'image11project'
    BLOB_STORAGE_KEY = os.environ.get('BLOB_STORAGE_KEY') or 'ZBv23gxLikRFMsYe/AhijCY4Dq0pyOHD9/VPI57kabNcylBhgrTlwlvR/jOj0WpJgGEZUYhNuKd8+AStM6A5JQ=='
    BLOB_CONTAINER = os.environ.get('BLOB_CONTAINER') or 'images'

    # Azure SQL Database
    SQL_SERVER = os.environ.get('SQL_SERVER') or 'cms1.database.windows.net'
    SQL_DATABASE = os.environ.get('SQL_DATABASE') or 'cms'
    SQL_USER_NAME = os.environ.get('SQL_USER_NAME') or 'cmsadmin'
    SQL_PASSWORD = os.environ.get('SQL_PASSWORD') or 'CMS4dmin'
    SQLALCHEMY_DATABASE_URI = (
        'mssql+pyodbc://' + SQL_USER_NAME + '@' + SQL_SERVER + ':' + SQL_PASSWORD
        + '@' + SQL_SERVER + ':1433/' + SQL_DATABASE
        + '?driver=ODBC+Driver+17+for+SQL+Server'
    )
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # Microsoft Authentication (MSAL)
    CLIENT_ID = os.environ.get('CLIENT_ID') or 'e1b24baf-e14a-438b-acc1-d3cd88871c80'
    CLIENT_SECRET = os.environ.get('CLIENT_SECRET') or 'xw98Q~3YdeTQ3HqqyjgpnoPdLxYtfrbNW0YUDbXb'
    AUTHORITY = os.environ.get('AUTHORITY') or "https://login.microsoftonline.com/common"
    REDIRECT_PATH = "/getAToken"
    SCOPE = ["User.Read"]
    SESSION_TYPE = "filesystem"
