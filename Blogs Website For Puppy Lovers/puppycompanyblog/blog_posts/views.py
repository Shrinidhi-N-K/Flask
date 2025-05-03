from flask import render_template,abort, url_for, flash, request, redirect, Blueprint, session
from flask_login import current_user,login_required
from puppycompanyblog import db
from puppycompanyblog.models import BlogPost
from puppycompanyblog.blog_posts.forms import BlogPostForm

blog_post = Blueprint('blog_post', __name__)

@blog_post.route('/create', methods=['GET','POST'])
@login_required
def create_post():

    form = BlogPostForm()

    if form.validate_on_submit():
        post = BlogPost(title=form.title.data,
                             text=form.text.data,
                             user_id=current_user.id)

        db.session.add(post)
        db.session.commit()
        flash('Blog Post Created!')
        return redirect(url_for('core.index'))

    return render_template('create_post.html', form=form)


@blog_post.route('/<int:blog_post_id>')
def view_post(blog_post_id):
    post = BlogPost.query.get_or_404(blog_post_id)
    return render_template('blog_post.html', title=post.title,
                           date=post.date,post=post)


@blog_post.route('/<int:blog_post_id>/update', methods=['GET','POST'])
@login_required
def update(blog_post_id):
    post = BlogPost.query.get_or_404(blog_post_id)
    if post.author != current_user:
        abort(403)

    form = BlogPostForm()

    if form.validate_on_submit():
        post.title=form.title.data
        post.text=form.text.data
        db.session.commit()

        flash('Blog Post Updated!')
        return redirect(url_for('blog_post.view_post',blog_post_id=post.id))

    elif request.method == 'GET':
        form.title.data = post.title
        form.text.data = post.text

    return render_template('create_post.html', title='UPDATING', form=form)


@blog_post.route('/<int:blog_post_id>/delete', methods=['GET','POST'])
@login_required
def delete_post(blog_post_id):
    post = BlogPost.query.get_or_404(blog_post_id)
    if post.author != current_user:
        abort(403)

    db.session.delete(post)
    db.session.commit()
    flash('Blog Deleted')
    return redirect(url_for('core.index'))