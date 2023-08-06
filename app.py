# import flask module
from flask import Flask

# instance of flask application
app = Flask(__name__)

from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_geek():
    return 'I love coding!! AWS is so awesome! :D Today is a sunday!'


if __name__ == "__main__":
    app.run(debug=True)
