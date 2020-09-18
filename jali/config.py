import os

JALI_PATH = os.path.dirname(os.path.abspath(__file__))
BASE_PATH = os.path.abspath(os.path.join(JALI_PATH, os.pardir))
ID = os.environ.get('id')
API_ID = os.environ.get('api_id')
API_HASH = os.environ.get('api_hash')
SQLALCHEMY_DATABASE_URI = os.environ.get('DB_URL', 'sqlite:///app.sqlite')
ADMIN = int(os.environ.get('admin', 529004070))
