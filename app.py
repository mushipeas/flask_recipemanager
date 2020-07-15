import os
from datetime import datetime

from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy


if "DATABASE_URL" in os.environ:
    DATABASE_URL = os.environ['DATABASE_URL'] + '/recipes'
else:
    DATABASE_URL = "postgresql://postgres:tempass@host.docker.internal/recipes"

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = DATABASE_URL
db = SQLAlchemy(app)


class Recipe(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    url = db.Column(db.String(300))
    title = db.Column(db.String(100), nullable=False)
    total_time_minutes = db.Column(db.Integer)
    yields = db.Column(db.String(50))
    ingredients = db.Column(db.String(2000), nullable=False)
    instructions = db.Column(db.String(6000), nullable=False)
    img_url = db.Column(db.String(300))
    desc = db.Column(db.String(300))

    def __repr__(self):
        return "<Recipe ID %r>" % self.id


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/search/", methods=["GET", "POST"])
def newsearch():
    search_params = request.args.to_dict()
    terms_ = search_params["terms"] if "terms" in search_params.keys() else None

    if "p" not in search_params.keys():
        search_params["p"] = "1"
    page = int(search_params["p"])

    if terms_:
        terms = ["%" + term + "%" for term in terms_.split()]
    else:
        terms = [""]

    results_ = db.session.query(Recipe)

    for term in terms:
        results_ = results_.filter(Recipe.title.like(term))

    results_per_page = 12
    result_offset = (page - 1) * results_per_page

    results_count = results_.count()
    results = results_.offset(result_offset).limit(results_per_page).all()

    print(results_count)

    return render_template(
        "new_search_res.html",
        results=results,
        results_count=results_count,
        **search_params,
        next_page=page + 1
    )


if __name__ == "__main__":

    app.run(debug=True)
