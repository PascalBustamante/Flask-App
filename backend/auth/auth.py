from flask import Blueprint, render_template, request, jsonify, redirect, url_for, session,flash
from database.models import User, db
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import login_user, login_required, logout_user, current_user
from flask_jwt_extended import create_access_token, jwt_required, get_jwt_identity


auth = Blueprint('auth', __name__, template_folder='templates', static_folder='static')




@auth.route('/login', methods=['POST'])

def login():
    email = request.json.get("email", None)
    password = request.json.get("password", None)
    if email != "test" or password != "test":
        return jsonify({"msg": "Bad username or password"},email), 401

    access_token = create_access_token(identity=email)
    return jsonify(access_token=access_token)

'''
def login():
    email = request.form.get('email')
    password = request.form.get('password')

    #user = User.query.filter_by(email=email).first()
    
    if email == "test":
        access_token = create_access_token(identity=email)
        return jsonify(access_token=access_token)

     if check_password_hash(user.password, password):
            access_token = create_access_token(identity=email)
            return jsonify(access_token=access_token)
        else:
            return jsonify({'msg': 'Incorrect email or password, try again.'}), 401
    else:
        return jsonify({'msg': 'Incorrect email or password, try again.'}), 401'''


@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('auth.login-test'))


@auth.route('/registration', methods=['GET', 'POST'])
def registration():
    if request.method == 'POST':
        email = request.form.get('email')
        username = request.form.get('username')
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')

        session['username'] = username
        session['email'] = email

        if not username or not email:
            
            return redirect(url_for('auth.sign_up'))

        user = User.query.filter_by(email=email).first()
        if user:
            flash('Email already exists.', category='error')
        elif len(email) < 4:
            flash('Email must be greater than 3 characters.', category='error')
        elif len(username) < 2:
            flash('First name must be greater than 1 character.', category='error')
        elif password1 != password2:
            flash('Passwords don\'t match.', category='error')
        elif len(password1) < 7:
            flash('Password must be at least 7 characters.', category='error')
        else:
            new_user = User(email=email, username=username, password=generate_password_hash(
                password1, method='sha256'))
            db.session.add(new_user)
            db.session.commit()
            login_user(new_user, remember=True)
            flash('Account created!', category='success')
            return redirect(url_for('views.home'))

    return render_template("sign_up.html", user=current_user)
