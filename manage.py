from app import create_app,db
from flask_script import Manager,Server
from app.models import User,Post,Comment,Role,PostCategory
from  flask_migrate import Migrate, MigrateCommand


# Creating app instance
app = create_app('development')
'''
development is for launching the app locally..please uncomment it when you want to run the app locally
'''
#app = create_app('production')
'''
production is for launching the app remotely..please uncomment it when you want to run the app remotely
'''

manager = Manager(app)
manager.add_command('server',Server)

migrate = Migrate(app,db)
manager.add_command('db',MigrateCommand)


@manager.shell
def make_shell_context():

    return dict(app = app,db = db,User = User,Post=Post,Comment=Comment,Role=Role,PostCategory=PostCategory)

if __name__ == '__main__':
    manager.run()