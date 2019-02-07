from flask import Flask
from flask import render_template, request, redirect, url_for, session

app = Flask(__name__)
app.debug = True
app.secret_key = b'_MZqRP5HJE&M5mBXZ*pu3fnf8Um%?m$7'


@app.route('/')
def index():
    """
    This is the main landing page for logged in users.

    :return: If session is invalid the user is redirected to the login page.
    """

    if 'username' in session:
        return 'Logged in'
    else:
        return redirect(url_for('login'))


@app.route('/login', methods=['POST', 'GET'])
def login():
    """
    Handles the user login.

    :return: Displays either user welcome page or redirects to login.
    """
    if request.method == 'GET':
        return render_template('login.html', attempted=False)
    else:
        if request.form['username'] == 'test':
            session['username'] = request.form['username']
            return redirect(url_for('index'))
        return render_template('login.html', attempted=True)


@app.route('/logout')
def logout():
    """
    Ends the session for the user.

    :return: Redirects to login page.
    """

    session.pop('username', None)
    return redirect(url_for('login'))


@app.route('/register', methods=['POST', 'GET'])
def register():
    """
    Handling user registration.

    :return: Redirects to login page.
    """
    if request.method == 'POST':
        print(request.form['first_name'],
              request.form['last_name'],
              request.form['email'],
              request.form['username'],
              request.form['password'])
        # TODO Add functionality to sanitize and add user information to db.
        return redirect(url_for('login'))
    return render_template('register.html')


@app.route('/forgot_password', methods=['POST', 'GET'])
def forgot_password():
    """
    Handling forgotten password.

    :return: Redirects to login page.
    """
    if request.method == 'POST':
        print(request.form['email'])
        # TODO Add functionality to reset password.
        return redirect(url_for('login'))
    return render_template('forgot_password.html')


if __name__ == '__main__':
    app.run(debug=True)
