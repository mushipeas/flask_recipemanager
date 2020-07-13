# Flask_taskmanager

My first project using Flask and SQLAlchemy.

This follows the FreeCodeCamp Tutorial: https://www.youtube.com/watch?v=Z1RJmh_OqeA

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

This should generate `test.db`.

## Start the app

Run the following in the root directory:

    python app.py
