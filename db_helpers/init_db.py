from flask import Flask
from flask_sqlalchemy import SQLAlchemy

DATABASE_URL = "sqlite:///../recipes.db"

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = DATABASE_URL
db = SQLAlchemy(app)

db.create_all()
