from flask import Flask
from flask_script import Manager
# the only  required argument to the flask  class constructor is the name of the
# main module or package of the application. For most applicaions, Python's __name__
# variable is the correct value
app = Flask(__name__)

manager = Manager(app)

# a route is declared using this decorator
@app.route('/')
def index():
    return '<h1>Hello World!</h1>'


@app.route('/user/<name>')
def user(name):
    return '<h1>Hello, %s</h1>' % name


if __name__== '__main__':
    manager.run()
