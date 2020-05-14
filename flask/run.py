# import os library
import os
# import flask class
from flask import Flask

# create an instance of flask class, the convention of the variable is called app
# The first argument of the Flask class is the name of the applications module - our package.
# __name__ is ta built-in Python variable, Flask needs this so that it knows where to look for templates and static files. 
app = Flask(__name__)

"""
use route decorator to tell Flask what URL should trigger the function as following
In Python, a decorator starts with the @ sign, which is also called pie notation. 
a decorator is a way of wrapping functions. 
"""
# "/" indicate the root directory 
# when we try to browse to the root directory as indicated by the "/", then flask triggers the index function underneath and returns the "Hello, World"
@app.route("/")
def index():
    return "Hello, World"

if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)