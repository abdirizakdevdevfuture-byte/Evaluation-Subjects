from configuration.config import db
from flask_login import UserMixin

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), nullable=False)
    password = db.Column(db.String(255), nullable=False)
    db.relationship('Subjects')

    def __repr__(self):
        return f'id:  {self.id} ,  UserName: {self.username}, email: {self.email}, password:  {self.password} '




class Subjects(db.Model):
    subject_id = db.Column(db.Integer, primary_key=True)
    ait= db.Column(db.String(2000), nullable=False)
    aad = db.Column(db.String(2000), nullable=False)
    rm = db.Column(db.String(2000), nullable=False)
    dccn= db.Column(db.String(2000), nullable=False)
    esd = db.Column(db.String(2000), nullable=False)
    de = db.Column(db.String(2000), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)


    def __repr__(self):
        return f'id:  {self.id}, AIT: {self.AIT}, AAD {self.AAD}, RM: {self.RM}, DCcN: {self.DCcN}, ESD: {self.ESD}, DE: {self.DE} '