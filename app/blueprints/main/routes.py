from flask import render_template, redirect, url_for
from . import bp as app
from flask_login import current_user
from app.blueprints.main.models import Car

@app.route("/")
def home():
    if not current_user.is_authenticated: 
        return redirect(url_for("auth.login"))
    sale = Car.query.all()
    sale.sort(key=lambda sale: sale.date_created, reverse = True)

    context = { 
        "sales": sale,
        "user": "Noface"
    }
    return render_template("index.html", **context)

@app.route("/about")
def about():
    return render_template("about.html")