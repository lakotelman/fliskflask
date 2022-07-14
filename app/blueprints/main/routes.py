from flask import render_template
from . import bp as app
from app.blueprints.main.models import Car

@app.route("/")
def home():
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