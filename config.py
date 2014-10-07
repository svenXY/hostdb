import os
basedir = os.path.abspath(os.path.dirname(__file__))

SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'app.db')
SQLALCHEMY_MIGRATE_REPO = os.path.join(basedir, 'db_repository')

WTF_CSRF_ENABLED = True
SECRET_KEY = 'adfrgs tzrtrwtrwwtzrwt rwwz wrtzw43565476 $%&/3556'

# pagination
HOSTS_PER_PAGE = 20
