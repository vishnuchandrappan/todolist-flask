# importing Flask class form flask package
from flask import Flask, render_template, request

# create an instance of flask
app = Flask(__name__)

# create a route with @app.route decorator.
'''
decorators can be used to inject additional functionality to one or more functions.
TWe can use various inbuilt decorators as well as create custom ones
'''


@app.route('/')
@app.route('/home')
def helloWorld():
    userName = 'chandler'
    isLoggedIn = True
    friends = ['joey', 'phoebe', 'ross', 'monica', 'rachel']
    return render_template('index.html', name=userName, isLoggedIn=isLoggedIn, friends=friends)


@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/contact')
def contact():
    return render_template('contact.html')


# API Routes

@app.route('/api')
def apiHome():
    return {
        "message": "Hello World"
    }


todos = [
    {
        "id": 1,
        "text": "Learn python",
        "isCompleted": True,
    },
    {
        "id": 2,
        "text": "Learn Flask",
        "isCompleted": False,
    },
    {
        "id": 3,
        "text": "Learn ML",
        "isCompleted": False,
    },
]


@app.route('/api/todos')
def todosIndex():
    return {
        "todos": todos
    }


# handling urlParams
@app.route('/api/todos/<todo>')
def todosShow(todo):
    return {
        "todo":  todo
    }


# handling queryParams
@app.route('/api/search')
def search():
    params = request.args
    return {
        "todos": todos,
        "params": params
    }


# handling bodyParams
@app.route('/api/todos', methods=['POST'])
def todosCreate():
    bodyParams = request.form
    return {
        "body_params": bodyParams
    }


if __name__ == '__main__':
    # for debug mode
    app.run(debug=True)
