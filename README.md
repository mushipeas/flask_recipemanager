# Flask_recipemanager

A recipe-manager with scraped data from https://www.bbcgoodfood.com

The initial data is present as json files under /recipes/.

The database has been migrated from sqlite (used in early production) to postgresql (heroku-postgresql, for the demo server).

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

    pip install -r requirements.txt

Development requirements (additional):

    pip install -r requirements-dev.txt

## Starting with existing sqlite db

Change `DATABASE_URL` in app.py to:
    DATABASE_URL = "sqlite:///recipes.db"

## Starting from scratch:

### Initialise the sqlite database
Change the database url as above (in 'starting with existing sqlite db' section).

Run:

    python initdb.py

### Populate recipes.db

Run:

    python populate_db.py [inputfile.json]

This will populate the db with `inputfile.json`. Sample files can be found under `./recipes`.

### Get images and descriptions

Run:

    python get_img_desc.py

The script will use the urls in the database to get image urls and update missing entries for these and the descriptions in the database rows.

## Migrating to postgres (or Heroku)

Follow the documentated steps in `sqlite_to_postgres migration.md`.

## Start the app

Run the following in the root directory:

    python app.py
