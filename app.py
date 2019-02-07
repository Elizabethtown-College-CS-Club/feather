from flask import Flask
from flask import render_template, request, redirect, url_for

app = Flask(__name__)
app.debug = True
app.secret_key = 'This is a random secret key.'


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/handle_login', methods=['POST'])
def handle_login():
    if request.form['username'] == 'test':
        return 'Test' + request.form['username'] + ' ' + request.form['password']
    else:
        return 'Wrong'


@app.route('/dashboard')
def dashboard():
    return 'Dashboard home'


if __name__ == '__main__':
    app.run()


"""
This app in its current status is very insecure. Further measure should be taken to protect the end user from exploits.
(CSRF)
"""
