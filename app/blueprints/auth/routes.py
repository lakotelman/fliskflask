from flask import flash, render_template, request, url_for, redirect
from . import bp as app
from app import db
from flask_login import login_user, logout_user, current_user
from app.blueprints.main.models import User


@app.route("/login", methods=["GET", "POST"])
def login():
    if current_user.is_authenticated:
        return redirect(url_for("main.home"))
    if request.method == "POST":
        user = User.query.filter_by(email=request.form["inputEmail"]).first()

        if user is None:
            flash(
                f"The user with email {request.form['inputEmail']} doesn't exist",
                "danger",
            )
        elif not user.check_my_pass(request.form["inputPassword"]):
            flash("Password is incorrect", "danger")
        else:
            login_user(user)
            flash(f"Welcome back, {user.first_name}.", "success")
            return redirect(url_for("main.home"))
        return render_template("login.html")
    else:
        return render_template("login.html")


@app.route("/register", methods=["GET", "POST"])
def register():
    if current_user.is_authenticated:
        return redirect(url_for("main.home"))
    if request.method == "POST":
        # Checks the db to see if the user already exists
        check_user = User.query.filter_by(email=request.form["inputEmail"]).first()
        if check_user is not None:
            flash("User with this email already exists.", "danger")
        else:
            # If the user doesn't exist, create a new one.
            # Make sure the passwords match, if so, create a new user.
            if request.form["inputPassword"] == request.form["inputPasswordConfirm"]:
                new_user = User(
                    email=request.form["inputEmail"],
                    username=request.form["inputUsername"],
                    first_name=request.form["inputFirstName"],
                    last_name=request.form["inputLastName"],
                )
                # hashes the user's password based on a function defined in the user class thanks to werkzueg
                new_user.hash_my_pass(request.form["inputPassword"])
                db.session.add(new_user)
                db.session.commit()
                flash("Welcome, new user. Please log in.", "success")
                return redirect(url_for("auth.login"))
            else:
                flash("Your passwords don't match.", "danger")
            # sends them back to registration page if they don't successfully register a user.
            return render_template("register.html")
    else:
        return render_template("register.html")

    return render_template("register.html")


@app.route("/logout")
def logout():
    logout_user()
    return redirect(url_for("auth.login"))
