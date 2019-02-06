from flask import Flask
from flask import Flask, flash, redirect, render_template, request, session, abort
from flask_mysqldb import MySQL
import os


app = Flask(__name__)

app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'password123'
app.config['MYSQL_DB'] = 'feather'
app.config['MYSQL_CURSORCLASS'] = 'DictCursor'

mysql = MySQL(app)


@app.route('/')
def home():
    if not session.get('logged_in'):
        return render_template('login.html')
    else:
        return "Homepage here"

@app.route('/login', methods=['POST'])
def do_admin_login():
    password = request.form['password']
    username = request.form['username']

    cursor = mysql.connection.cursor()
    cursor.execute("SELECT * FROM USERS WHERE USERNAME = \"" + username + "\";")
    queryresult = cursor.fetchall()
    print(queryresult)





    if queryresult[0].get("password") == password:
        session['logged_in'] = True
        return home()
    else:
        return 'wrong password'

if __name__ == "__main__":
    app.secret_key = os.urandom(12)
    app.run(debug=True,host='0.0.0.0', port=8080)