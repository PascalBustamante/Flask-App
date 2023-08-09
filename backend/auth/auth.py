from flask import Blueprint, render_template, request, jsonify, redirect, url_for, session,flash
from database.models import User, db
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import login_user, login_required, logout_user, current_user
from flask_jwt_extended import create_access_token, jwt_required, get_jwt_identity
from flask_bcrypt import generate_password_hash, check_password_hash


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


@auth.route('/registration', methods=['POST'])
def registration():
    if request.method == 'POST':
        email = request.form.get('email')
        ##username = request.form.get('username')
        password = request.form.get('password') 
        #confirm_password = request.form.get('confirm-password') #this can be handled by the frontend

        user_exists = User.query.filter_by(email=email).first() is not None

        if user_exists:
            return jsonify({'error': 'Email already exists'}), 409
        
        hashed_password = generate_password_hash(password=password)
        new_user = User(email=email, password=hashed_password)
        db.add(new_user)
        db.commit() 
        
        return jsonify({
            'id': new_user.id,
            'email': new_user.email
        })
    
@auth.route('/login', methods=['POST'])
def login():
    email = request.json.get("email", None)
    password = request.json.get("password", None)
    if email != "test" or password != "test":
        return jsonify({"msg": "Bad username or password"},email), 401

    access_token = create_access_token(identity=email)
    return jsonify(access_token=access_token)