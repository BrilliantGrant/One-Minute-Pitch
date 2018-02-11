from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField,SubmitField,BooleanField,RadioField,SelectField,FileField,PasswordField,SelectField
from wtforms.validators import Required

class PitchForm(FlaskForm):
    title = StringField('Pitch Title',validators=[Required()])
    body =TextAreaField('Pitch Content',validators=[Required()])
    category =SelectField('choose from the following categories', choices=[('pick_up','pick-up '), ('interview Pitch','interview Pitch'),
        ('product pitch', 'product pitch'), ('promotion pitch', 'promotion pitch')],validators=[Required()])
    submit = SubmitField('Submit')


class CommentsForm(FlaskForm):
    comment = TextAreaField('Comment', validators=[Required()])
    vote = RadioField('Vote ',choices=[('upvote','upvote'),('downvote','downvote')],validators=[Required()])                                       
    submit = SubmitField('SUBMIT') 



