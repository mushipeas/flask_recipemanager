# Flask_recipemanager

A recipe-manager with scraped data from https://www.bbcgoodfood.com

The initial data is present as json files under /recipes/.

Multiple scripts have been set up to scrape additional data from the site (using beautifulsoup4), where initial data was missing. ie. fetching image urls and descriptions, and associating them to items in the database.

A demo can be seen at:
https://damp-reef-19532.herokuapp.com/

## Setup

Start a virtual environment in the base directory:

    python -m venv .venv

Activate the environment:

    .\.venv\Scripts\activate (Windows)
    source .venv/bin/activate (UNIX)

Install requirements:

    pip install .

## Initialise the sqlite database

Open the python shell in the root directory:
    
    >>> from app import db
    >>> db.create_all()

This should generate `recipes.db`.

Alternatively, run `initdb.py`.

## Populate recipes.db

Run:

    python populate_db.py [inputfile.json]

This will populate the db with `inputfile.json`. Sample files can be found under `./recipes`.

## Get images and descriptions

Run:

    python get_img_desc.py

The script will use the urls in the database to get image urls and update missing entries for these and the descriptions in the database rows.

## Start the app

Run the following in the root directory:

    python app.py
