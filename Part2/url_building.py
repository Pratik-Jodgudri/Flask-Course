import time
from flask import Flask, redirect, url_for

app = Flask(__name__)

@app.route('/')
def home():
    return "<h1>Welcome to Home Page!</h1>"

@app.route('/score/<name>/<int:num>')
def score(name, num):
    if num < 30:
        time.sleep(1)
        return redirect(url_for('failed', name = name, num = num))
    else:
        time.sleep(1)
        return redirect(url_for('passed', name = name, num = num))

@app.route('/pass/<name>/<int:num>')
def passed(name, num):
    return f"<h1>Congratulations {name.title()}! You have Passed with {num} marks!</h1>"

@app.route('/fail/<name>/<int:num>')
def failed(name, num):
    return f"<h1>Sorry {name.title()}, You've Failed with {num} marks!</h1>"

if __name__ == '__main__':
    app.run(debug=True)