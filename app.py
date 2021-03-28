import os
from flask import Flask

# We need this so that it can import for Heroku
if os.path.exists('env.py'):
    import env


app = Flask(__name__)


@app.route('/')
def hello():
    return 'Hello World ... again!'


# Get info from env.py
if __name__ == '__main__':
    app.run(host = os.environ.get('IP'),
            port = int(os.environ.get('PORT')),
            debug = True) # Make sure to change this to false during project deployment
