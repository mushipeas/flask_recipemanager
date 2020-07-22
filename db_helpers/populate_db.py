import json
import sys

from init_db import db

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


def to_recipe_model(recipe):

    return Recipe(
        url=recipe["URL"],
        title=recipe["title"],
        total_time_minutes=recipe["total_time"],
        yields=recipe["yields"],
        ingredients=str(recipe["ingredients"]),
        instructions=recipe["instructions"],
    )


if __name__ == "__main__":

    try:
        input_file = sys.argv[1]
    except:
        print("Error: Please provide an input file.")
    else:
        with open(input_file) as file:
            recipes = json.load(file)

        recipe_models = [to_recipe_model(recipe) for recipe in recipes]

        db.session.bulk_save_objects(recipe_models)
        db.session.commit()
