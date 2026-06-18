from  configuration.config import db, app
from flask import (render_template,
                   redirect, request, url_for, Blueprint, flash, jsonify, session)
from models.db import Subjects
from models.db import User

Admin_bp = Blueprint("Admin_bp", __name__,  template_folder="templates", static_folder="static")



@Admin_bp.route('/Home')
def admin_home():
    users = User.query.all()
    SubVotes = Subjects.query.all()
    return render_template('admin.html', users=users, SubVotes=SubVotes)



@Admin_bp.route('/evaluators', methods=['GET', 'POST'])
def evaluators():
    if request.method == 'POST':
        ait = request.form["ait"]
        aad = request.form["aad"]
        rm = request.form["rm"]
        dccn = request.form["dccn"]
        esd = request.form["esd"]
        de = request.form["de"]

        user_id = session.get("user_id")

        new_vote = Subjects(ait=ait, aad=aad, rm=rm, dccn=dccn, esd=esd, de=de, user_id=user_id)
        db.session.add(new_vote)
        db.session.commit()

        flash("waa maad santay Xogtada waala God biyey", category="success")
        return redirect(url_for("users_bp.evaluation"))


    return  render_template('evaluators.html')


@Admin_bp.route('/Users')
def users():
    users = User.query.all()
    return render_template('users.html', users=users)





@Admin_bp.route('/Evaluators')
def view_votes():
    votes = Subjects.query.all()
    return render_template('votes.html', votes=votes)








