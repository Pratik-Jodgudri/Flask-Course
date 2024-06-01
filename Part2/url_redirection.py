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
        return redirect(url_for('failed'))
    else:
        time.sleep(1)
        return redirect(url_for('passed'))

@app.route('/pass')
def passed():
    return "<h1>Congratulations! You have Passed!</h1>"

@app.route('/fail')
def failed():
    return "<h1>Sorry, You've Failed!</h1>"

if __name__ == '__main__':
    app.run(debug=True)