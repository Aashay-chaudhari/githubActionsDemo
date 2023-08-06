# import flask module
from flask import Flask

# instance of flask application
app = Flask(__name__)

from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_geek():
    return 'Am I god or am I?!'


if __name__ == "__main__":
    app.run(debug=True)
