import os
basedir = os.path.abspath(os.path.dirname(__file__))

class Config:
    HOSTS_PER_PAGE = 20
    WTF_CSRF_ENABLED = True
    SECRET_KEY = os.environ.get('SECRET_KEY') or '5b6e4e276129488ba5fff55310960742'
    SSL_DISABLE = True
    SQLALCHEMY_COMMIT_ON_TEARDOWN = True
    SQLALCHEMY_RECORD_QUERIES = True
    MAIL_SERVER = 'localhost'
    MAIL_PORT = 25
    MAIL_SUBJECT_PREFIX = '[HostDB]'
    MAIL_SENDER = 'HostDB Admin <hostdb@example.com>'
    MAIL_ADMIN = 'hostdb-admin@example.com'
    #ADMIN = os.environ.get('FLASKY_ADMIN')
    TIMEZONE = 'Europe/Berlin'

    @staticmethod
    def init_app(app):
        pass


class DevelopmentConfig(Config):
    DEBUG = True
    SQLALCHEMY_ECHO = True
    TIMEZONE = 'NAIVE'
    SQLALCHEMY_DATABASE_URI = os.environ.get('DEV_DATABASE_URL') or \
        'sqlite:///' + os.path.join(basedir, 'hostdb-dev.sqlite') + '?check_same_thread=False'


class TestingConfig(Config):
    TESTING = True
    SQLALCHEMY_DATABASE_URI = os.environ.get('TEST_DATABASE_URL') or \
        'sqlite:///' + os.path.join(basedir, 'hostdb-test.sqlite')
    WTF_CSRF_ENABLED = False


class ProductionConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'postgresql://hostdb:password@localhost:5432/hostdb'

    #@classmethod
    #def init_app(cls, app):
    #    Config.init_app(app)

    #    # email errors to the administrators
    #    import logging
    #    from logging.handlers import SMTPHandler
    #    credentials = None
    #    secure = None
    #    if getattr(cls, 'MAIL_USERNAME', None) is not None:
    #        credentials = (cls.MAIL_USERNAME, cls.MAIL_PASSWORD)
    #        if getattr(cls, 'MAIL_USE_TLS', None):
    #            secure = ()
    #    mail_handler = SMTPHandler(
    #        mailhost=(cls.MAIL_SERVER, cls.MAIL_PORT),
    #        fromaddr=cls.FLASKY_MAIL_SENDER,
    #        toaddrs=[cls.FLASKY_ADMIN],
    #        subject=cls.FLASKY_MAIL_SUBJECT_PREFIX + ' Application Error',
    #        credentials=credentials,
    #        secure=secure)
    #    mail_handler.setLevel(logging.ERROR)
    #    app.logger.addHandler(mail_handler)


class HerokuConfig(ProductionConfig):
    SSL_DISABLE = bool(os.environ.get('SSL_DISABLE'))

    @classmethod
    def init_app(cls, app):
        ProductionConfig.init_app(app)

        # handle proxy server headers
        from werkzeug.contrib.fixers import ProxyFix
        app.wsgi_app = ProxyFix(app.wsgi_app)

        # log to stderr
        import logging
        from logging import StreamHandler
        file_handler = StreamHandler()
        file_handler.setLevel(logging.WARNING)
        app.logger.addHandler(file_handler)


class UnixConfig(ProductionConfig):
    @classmethod
    def init_app(cls, app):
        ProductionConfig.init_app(app)

        # log to syslog
        import logging
        from logging.handlers import SysLogHandler
        syslog_handler = SysLogHandler()
        syslog_handler.setLevel(logging.WARNING)
        app.logger.addHandler(syslog_handler)


config = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'production': ProductionConfig,
    'heroku': HerokuConfig,
    'unix': UnixConfig,

    'default': DevelopmentConfig
}
