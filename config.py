import os
basedir = os.path.abspath(os.path.dirname(__file__))
#数据库配置\
SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'app.db')
SQLALCHEMY_MIGRATE_REPO = os.path.join(basedir, 'db_repository')
SQLALCHEMY_RECORD_QUERIES = True
DATABASE_QUERY_TIMEOUT = 0.5


#表单验证配置
CSRF_ENABLED = True
SECRET_KEY = 'you-will-never-guess'