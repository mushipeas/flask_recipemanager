import json
import sys

from app import db, Recipe


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

    input_file = sys.argv[1]

    with open(input_file) as file:
        recipes = json.load(file)

    recipe_models = [to_recipe_model(recipe) for recipe in recipes]

    db.session.bulk_save_objects(recipe_models)
    db.session.commit()
