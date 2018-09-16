from flask import render_template, request, redirect, url_for, abort
from . import main
from .forms import CommentsForm, UpdateProfile, PostForm, UpvoteForm
from ..models import Comment, Post, User,Role,PostCategory
from flask_login import login_required, current_user
from .. import db



@main.route('/')
def index():
    '''
   view function that defines the routes decorater for the index
    '''



    title = 'Home - Welcome to The best Movie Review Website Online'

    return render_template ( 'index.html' , title=title)


#  end of index root functions


@main.route ( '/inspiration/posts/' )
def inspiration():
    '''
    View root page function that returns the index page and its data
    '''
    title = 'inspiration'

    posts = Post.get_all_posts()

    return render_template ('inspiration.html', title=title, posts=posts)


#  end of Inspiration root functions


@main.route ('/Editors/posts/')
def Editors():
    '''
    View root page function that returns the index page and its data
    '''
    title = 'promotion posts'

    posts = Post.get_all_posts ( )

    return render_template ( 'Editors.html' , title=title , posts=posts )

#  end of promotion root functions


@main.route ( '/Education/posts/' )
def Education():
    '''
    View root page function that returns the index page and its data
    '''
    title = 'Product posts'
    posts = Post.get_all_posts ( )
    return render_template ( 'Education.html' , title=title , posts=posts )


#  end of Education root functions

@main.route ( '/News/posts/' )
def News():
    '''
    View root page function that returns the index page and its data
    '''
    title = 'Product Pitches'
    posts = Post.get_all_posts ( )
    return render_template ( 'News.html' , title=title , posts=posts )

#  end of News root functions

@main.route('/post/<int:post_id>')
def post(post_id):

    '''
    View pitch page function that returns the post details page and its data
    '''
    found_post= get_post(post_id)
    title = post_id
    post_comments = Comment.get_comments(post_id)

    return render_template('post.html',title= title ,found_post= found_post, post_comments= post_comments)

@main.route('/search/<post_name>')
def search(post_name):
    '''
    View function to display the search results
    '''
    searched_posts = search_post(post_name)
    title = f'search results for {post_name}'

    return render_template('search.html',title=title,posts= searched_posts)


@main.route('/post/new/', methods = ['GET','POST'])
@login_required
def new_post():
    '''
    Function that creates new posts
    '''
    form = PostForm()


    if category is None:
        abort( 404 )

    if form.validate_on_submit():
        post= form.content.data
        category_id = form.category_id.data
        new_post= Post(post= post, category_id= category_id)

        new_post.save_pitch()
        return redirect(url_for('main.index'))

    return render_template('new_post.html', new_PostForm= form, category= category)


@main.route('/category/<int:id>')
def category(id):
    '''
    function that returns posts based on the entered category id
    '''
    category = PostCategory.query.get(id)

    if category is None:
        abort(404)

    posts_in_category = Post.get_post(id)
    return render_template('category.html' ,category= category, postss= posts_in_category)

@main.route('/post/comments/new/<int:id>',methods = ['GET','POST'])
@login_required
def new_comment(id):
    form = CommentsForm()
    vote_form = UpvoteForm()
    if form.validate_on_submit():
        new_comment = Comment(post_id =id,comment=form.comment.data,username=current_user.username,votes=form.vote.data)
        new_comment.save_comment()
        return redirect(url_for('main.index'))
    #title = f'{pitch_result.id} review'
    return render_template('new_comment.html',comment_form=form, vote_form= vote_form)

@main.route('/user/<uname>/update/pic',methods= ['POST'])
@login_required
def update_pic(uname):
    user = User.query.filter_by(username = uname).first()
    if 'photo' in request.files:
        filename = photos.save(request.files['photo'])
        path = f'photos/{filename}'
        user.profile_pic_path = path
        db.session.commit()
    return redirect(url_for('main.profile',uname=uname))

@main.route('/user/<uname>')
def profile(uname):
    user = User.query.filter_by(username = uname).first()

    if user is None:
        abort(404)

    return render_template("profile/profile.html", user = user)


@main.route ( '/user/<uname>/update' , methods=['GET' , 'POST'] )
@login_required
def update_profile(uname):
    user = User.query.filter_by ( username=uname ).first ( )
    if user is None:
        abort ( 404 )

    form = UpdateProfile ( )

    if form.validate_on_submit ( ):
        user.bio = form.bio.data

        db.session.add ( user )
        db.session.commit ( )

        return redirect ( url_for ( '.profile' , uname=user.username ) )

    return render_template ( 'profile/update.html' , form=form )

@main.route('/view/comment/<int:id>')
def view_comments(id):
    '''
    Function that returs  the comments belonging to a particular pitch
    '''
    comments = Comment.get_comments(id)
    return render_template('view_comments.html',comments = comments, id=id)


@main.route('/test/<int:id>')
def test(id):
    '''
    this is route for basic testing
    '''
    post =Post.query.filter_by(id=1).first()
    return render_template('test.html',post= post)
