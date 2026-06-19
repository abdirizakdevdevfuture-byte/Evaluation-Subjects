from flask_sqlalchemy import SQLAlchemy
from flask import Flask
import os

app = Flask(__name__, template_folder="../templates", static_folder="../static")

# Use PostgreSQL on Render, fallback to SQLite for local dev
database_url = os.environ.get("DATABASE_URL", "sqlite:///evaluation.db")

# Render gives URLs starting with "postgres://" but SQLAlchemy needs "postgresql://"
if database_url.startswith("postgres://"):
    database_url = database_url.replace("postgres://", "postgresql://", 1)

app.config["SQLALCHEMY_DATABASE_URI"] = database_url
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False  # also fixed typo: MODIFICATION -> MODIFICATIONS
app.config["SECRET_KEY"] = os.environ.get("SECRET_KEY", "dev-dev-future")

db = SQLAlchemy(app)