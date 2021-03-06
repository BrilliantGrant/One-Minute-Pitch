from . import db
from werkzeug.security import generate_password_hash,check_password_hash
from flask_login import UserMixin
from . import login_manager

@login_manager.user_loader
def load_user(user_id):
	return User.query.get(int(user_id))




class User(UserMixin,db.Model):
	__tablename__ = 'users'
	id = db.Column(db.Integer,primary_key = True)
	username = db .Column(db.String(255))
	email = db.Column(db.String(255), unique = True, index = True)
	password_hash = db.Column(db.String(255))


	@property
	def password(self, password):
		raise AttributeError('You Cannot Read the password attribute')

	@password.setter
	def password(self, password):
		self.password_hash = generate_password_hash(password)


	def verify_password(self,password):
		return check_password_hash(self.password_hash,password)


	def __repr__(self):
		return f'User {self.username}'



class Pitch(db.Model):
    __tablename_='pitches'
    id = db.Column(db.Integer,primary_key = True)
    category = db.Column(db.String(255))
    title = db.Column(db.String(255))
    body = db.Column(db.String())
    
    def save_pitches(self):
        db.session.add(self)
        db.session.commit()

    @classmethod
    def get_pitches(cls):
        pitches = Pitch.query.all() 
        return pitches

    @classmethod
    def get_categories(cls, category):
        pitch_cat = Pitch.query.filter_by(category=category)
        return pitch_cat

    def __init__(self,title, body, category):
        self.title= title
        self.body= body
        self.category= category



class Comment(db.Model):
    
    __tablename__ = 'comments'

    id = db.Column(db.Integer,primary_key = True)
    comment= db.Column(db.String)
    pitches_id = db.Column(db.Integer,db.ForeignKey('pitch.id'))
    username =  db.Column(db.String)
    votes= db.Column(db.Integer)
    

    def save_comment(self):
        '''
        Function that saves comments
        '''
        db.session.add(self)
        db.session.commit()

    @classmethod
    def clear_comments(cls):
        Comment.all_comments.clear()

