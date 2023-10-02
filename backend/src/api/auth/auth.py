from flask import (
    Blueprint,
    render_template,
    request,
    jsonify,
    redirect,
    url_for,
    flash,
    current_app,
)


from database.models.user import User
from create_app import db_manager as db
from werkzeug.security import generate_password_hash, check_password_hash
from flask_jwt_extended import create_access_token, jwt_required, get_jwt_identity
from flask_bcrypt import generate_password_hash, check_password_hash


auth = Blueprint("auth", __name__, template_folder="templates", static_folder="static")


@auth.route("/registration", methods=["POST"])
def registration():
    if request.method == "POST":
        data = request.json
        username = data.get("username")
        email = data.get("email")
        password = data.get("password")

        user_exists = User.query.filter_by(email=email).first() is not None

        if user_exists:
            return jsonify({"error": "Email already exists"}), 409

        hashed_password = generate_password_hash(password=password).decode(
            "utf-8", "ignore"
        )
        new_user = User(
            email=email, username=username, password=hashed_password, role="user"
        )
        db.session.add(new_user)
        db.session.commit()

        return jsonify(
            {
                "id": new_user.id,
                "email": new_user.email,
                "username": username,
                "role": "user",
            }
        )


@auth.route("/login", methods=["POST"])
def login():
    email = request.json.get("email", None)
    password = request.json.get("password", None)

    user = User.query.filter_by(email=email).first()

    if user is None:
        return jsonify({"error": "User does not exist."})

    if check_password_hash(user.password, password):
        access_token = create_access_token(identity=email)
        return jsonify(access_token=access_token)

    if email != "test" or password != "test":
        return jsonify({"msg": "Bad username or password"}, email), 401
