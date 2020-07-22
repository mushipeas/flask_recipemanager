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

The system is currently set up to work with the database migrated to postgresql.

## Starting with existing sqlite db

Change `DATABASE_URL` in app.py to:
    DATABASE_URL = "sqlite:///recipes.db"

## Migrating to postgres (or Heroku)

Follow the documentated steps in `sqlite_to_postgres migration.md`.
This will migrate the sqlite data to your personal postgresql database.

## Start the app

Run the following in the root directory:

    python app.py
