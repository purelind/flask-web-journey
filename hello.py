from flask import Flask, render_template
from flask_script import Manager
from flask_bootstrap import Bootstrap
# the only  required argument to the flask  class constructor is the name of the
# main module or package of the application. For most applicaions, Python's __name__
# variable is the correct value
app = Flask(__name__)

manager = Manager(app)
bootstrap = Bootstrap(app)

# a route is declared using this decorator
@app.route('/')
def index():
    return render_template('index.html')


@app.route('/user/<name>')
def user(name):
    return render_template('user.html', name=name)


if __name__== '__main__':
    manager.run()
