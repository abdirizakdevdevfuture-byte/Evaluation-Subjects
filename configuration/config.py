from flask_sqlalchemy import  SQLAlchemy
from flask import Flask

app = Flask(__name__, template_folder="../templates", static_folder="../static")

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///evaluation.db"
app.config["SQLALCHEMY_TRACK_MODIFICATION"] = False
app.config["SECRET_KEY"] = "dev-dev-future"


db = SQLAlchemy(app)
