from flask import jsonify, request, redirect, flash
from . import bp as app
from app.blueprints.main.models import Car
from app import db
from flask_login import current_user


@app.route("/post-car", methods=["POST"])
def post_car():
    # retrieve data from request
    year = request.form["inputYear"]
    make = request.form["inputMake"]
    model = request.form["inputModel"]
    color = request.form["inputColor"]
    description = request.form["inputDescription"]
    price = float(request.form["inputPrice"])
    user = current_user.id

    # instantiate a new post
    new_sale = Car(
        year=year,
        make=make,
        model=model,
        color=color,
        description = description,
        price= price, 
        user_id= user
    )

    # add it to the database
    db.session.add(new_sale)
    db.session.commit()
    flash("New post created", "success")
    return redirect("http://127.0.0.1:5000")
