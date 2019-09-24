from flask import render_template,request,redirect,url_for,abort
from flask_login import login_required,current_user
from . import main
from .forms import UpdateProfile,PostAblog,PostAComment
from .. import db,photos
from ..models import User,blog,Comment

@main.route('/')
def landingpage():

    return render_template('index.html')

@main.route('/timeline',methods=['GET','POST'])
@login_required
def timeline():
    form = PostAblog()
    if form.validate_on_submit():
        new_blog = blog(upvotes=0,downvotes=0,title=form.title.data,content=form.content.data,user_id=current_user.id)
        new_blog.save_blog()
        return redirect(url_for('main.timeline'))
    blog= blog.get_blog()
    users = User.query.all()

    return render_template('timeline.html',form=form,blog=blog,users=users)
 
@main.route('/user/profile/<uname>')
@login_required
def profile(uname):
    user = User.query.filter_by(username = uname).first()

    if user is None:
        abort(404)
    blog = blog.query.order_by(blog.posted.desc()).all()
    
    return render_template('profile.html', user = user, blog=blog)

@main.route('/user/<uname>/update',methods = ['GET','POST'])
@login_required
def update_profile(uname):
    user = User.query.filter_by(username = uname).first()
    
    if user is None:
        abort(404)
    form = UpdateProfile()

    if form.validate_on_submit():
        user.bio = form.bio.data
        db.session.add(user)
        db.session.commit()

        return redirect(url_for('.profile',uname=user.username))

    return render_template('profile.html',form=form,user =user)

@main.route('/user/<uname>/update/pic',methods= ['POST'])
@login_required
def update_pic(uname):
    user = User.query.filter_by(username = uname).first()
    if 'photo' in request.files:
        filename = photos.save(request.files['photo'])
        path = f'photos/{filename}'
        user.profile_pic_path = path
        db.session.commit()
    return redirect(url_for('main.update_profile',uname=uname))

@main.route('/blog/new', methods=['GET', 'POST'])
@login_required
def new_blog():
    blog_form = PostAblog()
    if blog_form.validate_on_submit():
        title = blog_form.title.data
        blog = blog_form.text.data

        # Updated blog instance
        new_blog = blog(blog_title=title, blog_content=blog, user=current_user)

        # Save blog method
        new_blog.save_blog()
        return redirect(url_for('.index'))

    title = 'New blog'
    return render_template('blog.html', title=title)


  

