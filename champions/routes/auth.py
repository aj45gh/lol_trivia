from flask import Blueprint, render_template, request


auth = Blueprint(
    'auth',
    __name__,
    url_prefix='/auth',
)


@auth.get('/login')
def login_get():
    return render_template('auth/login.html')


@auth.post('/login')
def login_post():
    errors = []

    username = request.form['username']
    password = request.form['password']

    if not username:
        errors.append('Username is required.')
    if not password:
        errors.append('Password is required.')

    if errors:
        return

    from champions.services import auth

    if not auth.verify_login(username, password):
        return ':('

    return ':)'


@auth.get('/register')
def register_get():
    return render_template('auth/register.html')


@auth.post('/register')
def register_post():
    errors = []

    username = request.form['username']
    password = request.form['password']
    confirm_password = request.form['confirm-password']

    if not username:
        errors.append('Username is required.')
    if not password:
        errors.append('Password is required.')
    if not confirm_password:
        errors.append('Password confirmation is required.')

    if confirm_password != password:
        errors.append('Password and confirmation must match.')

    if errors:
        return ':O'

    from champions.services import auth

    if not auth.add_user(username, password):
        return ':('

    return ':)'
