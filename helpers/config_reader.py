import ConfigParser

CONFIG = ConfigParser.ConfigParser()
CONFIG.read('config.ini')

GLOBAL_PATH = CONFIG.get('global', 'path')
DEBUG = CONFIG.getboolean('global', 'debug')
SECRET_KEY = CONFIG.get('global', 'secret_key')

DB_NAME = CONFIG.get('database', 'name')

GITHUB_CLIENT_ID = CONFIG.get('github', 'client_id')
GITHUB_CLIENT_SECRET = CONFIG.get('github', 'client_secret')
