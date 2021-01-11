# importing Flask class form flask package
from flask import Flask

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
    return "Hello World"


@app.route('/about')
def about():
    return "About Us"


@app.route('/contact')
def contact():
    return "Contact Us"


if __name__ == '__main__':
    # for debug mode
    app.run(debug=True)
