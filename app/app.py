from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():
    #return render_template('index.html', title='My Firts Web App')
    data = {
        'title': 'My First Web App',
        'user_name' : 'Jhordan',
        'user_age' : 25
    }
    return render_template('index.html', data=data)

@app.route('/contact')
def contact():
    data = {
        'title': 'Contact',
        'user_name' : 'Jhordan',
        'user_age' : 25
    }
    return render_template('contact.html', data=data)

@app.route('/greeting/<user_name>')
def greeting(user_name):
    return f'!Hi, {user_name}!'

@app.route('/sum/<int:value1>/<int:value2>')
def sum(value1, value2):
    return "The sum is: " + str(value1 + value2)

@app.route('/profile/<user_name>/<int:age>')
def profile(user_name, age :int):
    return 'Your name is {0} and your age is {1} years old'.format(user_name, age)

def helloWorld():
    return {
        "Gretting": "Hello Nly"
    }


if __name__ == '__main__':
    app.add_url_rule('/hello', view_func=helloWorld)
    app.run(debug=True, port=5000)
