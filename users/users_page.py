from flask import blueprints, Blueprint, render_template, session, request, redirect, url_for


users_bp = Blueprint('users_bp', __name__, template_folder='templates', static_folder='static')





@users_bp.route('/evaluation', methods=['GET', 'POST'])
def evaluation():
    username = session.get("username")

    return render_template('evaluation.html', username=username)






