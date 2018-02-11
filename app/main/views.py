from . import main
from flask import render_template,request,redirect, url_for, abort
from flask_login import login_required,current_user
from ..models import Pitch,User,Comment
from .forms import PitchForm, CommentsForm

from .. import db


@main.route('/')
def index():
    '''
    View root page function that returns the index page and its data
    '''
    title = 'Home - Welcome to The best Pitching Website Online'


    # pitches = pitch.query.filter_by(category='glee').all()
    # print(pitches)
    pick_up = Pitch.query.filter_by(category = 'pick_up').all()
    interview = Pitch.query.filter_by(category = 'interview Pitch').all()
    product = Pitch.query.filter_by(category = 'product pitch').all()
    promotion = Pitch.query.filter_by(category = 'promotion pitch').all()
    comment = Comment.query.all()

    print(interview)

    return render_template('index.html',title=title,product = product,interview =interview,pick_up = pick_up, comment = comment)

@main.route('/newpitch' ,methods = ['GET','POST'])
@login_required
def new_pitch():

    form = PitchForm()

    if form.validate_on_submit():
        pitches = Pitch(title = form.title.data,body = form.body.data,category = form.category.data)

        pitches.save_pitches()
        # print('Your Pitch has been succenssfully saved!')
        return redirect(url_for('main.index'))

    return render_template('newpitch.html', pitch_form = form)


@main.route('/pitch/comments/new',methods = ['GET','POST'])
@login_required
def new_comment():
    form = CommentsForm()          
    # vote_form = UpvoteForm()
    if form.validate_on_submit():
        new_comment = Comment(comment=form.comment.data,username=current_user.username)
        new_comment.save_comment()
        return redirect(url_for('main.index'))
    #title = f'{pitch_result.id} review'
    return render_template('new_comment.html',comment_form=form,vote_form = form)

