from flask import render_template,g,redirect,url_for,session,request,flash
from flask_login import login_user, logout_user, current_user, login_required
from .forms import LoginForm
from .models import User
from APP import app,lm,db


@app.before_request
def before_request():
    g.user = current_user

@lm.user_loader
def load_user(id):
    return User.query.get(int(id))


@app.route('/')
@login_required
def index():
    return render_template('show.html')

@app.route('/login',methods=['GET', 'POST'])
def login():
    if g.user is not None and g.user.is_authenticated:
        return redirect(url_for('index'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.UserName.data).first()
        if user is not None and user.verify_password(form.PassWord.data):
            session['remember_me'] = form.remember_me.data
            login_user(user, form.remember_me.data)
            return redirect(request.args.get('next') or url_for('show'))
        flash('Invalid username or password.')
    return render_template('login2.html',
                           title='Sign In',
                           form=form)

@app.route('/show')
@login_required
def show():
    return render_template('show.html')

@app.route('/add')
@login_required
def add():
    return render_template('add.html')

@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))

@app.errorhandler(404)
def internal_error(error):
    return redirect(url_for('index'))

@app.errorhandler(500)
def internal_error(error):
    db.session.rollback()
    return redirect(url_for('index'))