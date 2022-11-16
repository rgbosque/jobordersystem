from flask import flash, redirect, render_template, url_for

from app import app
from app.forms import LoginForm


@app.route('/')
def home():
    return render_template("index.html", title="Home")

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash('Login requested for user {}, remember_me = {}'.format(form.username.data, form.remember_me.data))
        return redirect(url_for('dashboard'))
    return render_template("login.html", title="Login", form=form)

@app.route('/dashboard')
def dashboard():
    return render_template("dashboard.html", title="Dashboard")

@app.route('/aboutus')
def about_us():
    return render_template("about_us.html", title="About Us")