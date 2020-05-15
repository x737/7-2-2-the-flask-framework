## Goal for this module
1. Creating and running a Flask application
2. Serving HTML, CSS, and JavaScript files from the backend
3. How to make our code reusable by using template logic
4. How to post data from HTML forms
5. And how to deploy our project using a platform called Heroku so that it's served externally for all the world to see

## Hello Flask
see run.py

## Rendering HTML code

1. instead of add html elements on text "hello world", import the render_template() function for Flask
2. Return HTML code from a Flask function, allow us to render HTML code from the server by returning a string that contains HTML tags

## Routing

1. allow us to swich between views using URLs by creating routes
2. add same routes in href = "" in links in html and to @app.route("/")
3. use template logic by using **Jinja templating language**. href = "{{url_for('index')}}"
4. calling this url_for() function that looks up the view called index or the view called about(), and then injects some text, which is the actual root.
5. 'url_for()' method basically works like shorthand in order to dynamically build urls

## Template inheritance

1. Template Inheritance Allows us to inherit code from other templates By creating a base template and using {% extends 'base.html' %} in a child template
2. {% block content %}
    <h1>About</h1>
    {% endblock %}
