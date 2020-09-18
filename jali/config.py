import os


ID = os.environ.get('id')
API_ID = os.environ.get('api_id')
API_HASH = os.environ.get('api_hash')
SQLALCHEMY_DATABASE_URI = os.environ.get('DB_URL', 'sqlite:///app.sqlite')
