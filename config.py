import os  

class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or '3b7d!@Ud4c1tyCMS#2025'

    BLOB_ACCOUNT = os.environ.get('BLOB_ACCOUNT') or 'image11project'
    BLOB_STORAGE_KEY = os.environ.get('BLOB_STORAGE_KEY') or 'your-storage-key'
    BLOB_CONTAINER = os.environ.get('BLOB_CONTAINER') or 'images'

    SQL_SERVER = os.environ.get('SQL_SERVER') or 'cms1.database.windows.net'
    SQL_DATABASE = os.environ.get('SQL_DATABASE') or 'cms'
    SQL_USER_NAME = os.environ.get('SQL_USER_NAME') or 'cmsadmin'
    SQL_PASSWORD = os.environ.get('SQL_PASSWORD') or 'CMS4dmin'

    CLIENT_ID = os.environ.get('CLIENT_ID') or 'e1b24baf-e14a-438b-acc1-d3cd88871c80'
    CLIENT_SECRET = os.environ.get('CLIENT_SECRET') or 'xw98Q~3YdeTQ3HqqyjgpnoPdLxYtfrbNW0YUDbXb'

    AUTHORITY = os.environ.get('AUTHORITY') or "https://login.microsoftonline.com/common"

    REDIRECT_PATH = "/getAToken"
    SCOPE = ["User.Read"]
    SESSION_TYPE = "filesystem"
