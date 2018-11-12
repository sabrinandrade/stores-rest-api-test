from flask import Flask, jsonify


# __name__ contains the relative path of the module we are currently using
app = Flask(__name__)


@app.route('/')  # http://www.mysite.com/, means the homepage of the app, endpoint
def home():
    # Flask cannot return dictionaries from an endpoint
    return jsonify({'message': 'Hello World'})


# For the file you run, the file is __main__
# If this file is imported, app.run() will not be executed; you can only have access to the variable
if __name__ == '__main__':
    app.run()
