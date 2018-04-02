from flask import Flask, request, redirect, render_template
import cgi
import re

app = Flask(__name__)

app.config['DEBUG'] = True

@app.route("/signup", methods=['POST'])
def signup():
    username_error = False
    password_error = False
    verify_error = False
    email_error = False
    username = request.form['username']
    password = request.form['password']
    verify = request.form['verify']
    email = request.form['email']
    if not username or ' ' in username or len(username) < 3 or len(username) > 20:
        username_error = True
    if not password or ' ' in password or len(password) < 3 or len(password) > 20:
        password_error = True
    if not password == verify:
        verify_error = True
    if not re.match(r'[^@]+@[^@]+\.[^@]+', email) and email:
        email_error = True
    if username_error or password_error or verify_error or email_error:
        return render_template("home.html", username = username, email = email, username_error = username_error, password_error = password_error, verify_error = verify_error, email_error = email_error)
    return render_template("welcome.html", username = username)

@app.route("/")
def home():
    return render_template("home.html")

app.run()