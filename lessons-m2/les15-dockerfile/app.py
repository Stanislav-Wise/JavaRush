from flask import Flask


app = Flask(__name__)

@app.route('/')
def home():
    return 'hello world111222333'


@app.route('/about/')
def about():
    return "I'm Bob"


@app.route('/contacts/')
def contacts():
    return "I live in Moscow"


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)
