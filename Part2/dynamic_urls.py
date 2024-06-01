from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "<h1>Welcome to Home Page!</h1>"

@app.route('/welcome/<name>')
def welcome(name):
    return f"<h1>Hi {name.title()}, Welcome to our page!</h1>"



if __name__ == '__main__':
    app.run(debug=True)