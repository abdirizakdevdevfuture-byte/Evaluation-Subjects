from flask import (Blueprint,
     render_template, request, redirect, url_for, flash, session)
from configuration.config import db
from models.db import User
from werkzeug.security import generate_password_hash, check_password_hash

Admin_email = "Ader@gmail.com"
Admin_pass = "Ader123"




auth = Blueprint('auth', __name__, template_folder='templates', static_folder='static')


@auth.route('/create_Account', methods=['POST'])
def create_account():
    if request.method == 'POST':
        username = request.form["username"]
        email = request.form["email"]
        password = request.form["password"]


        new_user = User(username=username, email=email, password=generate_password_hash(password))
        db.session.add(new_user)
        db.session.commit()

        return redirect(url_for("auth.sing_up"))

    return render_template("index.html")


@auth.route('/sing_up', methods=['GET', 'POST'])
def sing_up():
    if request.method == 'POST':
        email = request.form["email"]
        password = request.form["password"]

        if email== Admin_email and password == Admin_pass:
            return redirect(url_for("Admin_bp.admin_home"))
        else:
            flash("Incorrect password", category="error" )



        found_user = User.query.filter_by(email=email).first()
        if found_user:
            if check_password_hash(found_user.password, password):
                session["username"] = found_user.username
                session["user_id"] = found_user.id

                flash("You have successfully signed up!", category="success" )
                return redirect(url_for("users_bp.evaluation"))
            else:
                flash("Incorrect password", category="error" )
                return redirect(url_for("auth.sing_up"))
        else:
            flash("Incorrect email ", category="error" )
            return redirect(url_for("auth.sing_up"))



    return render_template("singUp.html")