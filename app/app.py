from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello, World!'


@app.route('/name/<name>')
def hello_name(name):
    return f'Hello, {name}!'


@app.route('/age/<int:age>')
def show_age(age):
    return f'You are {age} years old.'


if __name__ == '__main__':
    app.run(debug=False)
# This is a test comment to trigger CI/CD workflow
