from flask import request, render_template, redirect, url_for, blueprints, flash
from configuration.config import db, app
from auth.authen import auth
from users.users_page import users_bp
from models.db import User
from Admin.Admin_core import Admin_bp

app.register_blueprint(auth, url_prefix="/Auth")
app.register_blueprint(users_bp, url_prefix="/Users")
app.register_blueprint(Admin_bp, url_prefix="/Admin")

# Create tables on import — runs both locally AND on Render/gunicorn
with app.app_context():
    db.create_all()

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/reset-db-xyz123')
def reset_db():
    db.drop_all()
    db.create_all()
    return "Database reset done!"


if __name__ == '__main__':
    app.run(debug=True)