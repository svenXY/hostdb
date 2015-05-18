from app import create_app, db
from app.models import Host, Role, Stage, Domain, User
from flask.ext.script import Manager, Shell
from flask.ext.migrate import Migrate, MigrateCommand

app = create_app('production')
manager = Manager(app)

migrate = Migrate(app, db)
manager.add_command('db', MigrateCommand)

import flask.ext.restless
restless = flask.ext.restless.APIManager(app, flask_sqlalchemy_db=db)
restless.create_api(Host, methods=['GET'], results_per_page=None)

def make_shell_context():
    return dict(app=app, db=db, User=User, Role=Role, Stage=Stage, Host=Host,
                Domain=Domain)
manager.add_command("shell", Shell(make_context=make_shell_context))
manager.add_command('db', MigrateCommand)

if __name__ == '__main__':
    manager.run()
