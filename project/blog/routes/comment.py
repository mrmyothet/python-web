from flask import Blueprint, request, render_template, redirect, url_for, flash
from flask_login import login_required, current_user
from ..models import db, Comment, Tweet

comment_routes = Blueprint("comment_routes", __name__)


# Route to add a comment to a tweet
@comment_routes.route("/tweets/<int:tweet_id>/comments", methods=["POST"])
@login_required
def add_comment(tweet_id):
    tweet = Tweet.query.get_or_404(tweet_id)
    content = request.form.get("content")
    if not content:
        flash("Comment cannot be empty.", "danger")
        return redirect(url_for("tweet_routes.view_tweet", tweet_id=tweet_id))

    new_comment = Comment(user_id=current_user.id, tweet_id=tweet_id, content=content)
    db.session.add(new_comment)
    db.session.commit()
    flash("Comment added successfully!", "success")
    return redirect(url_for("tweet_routes.view_tweet", tweet_id=tweet_id))


# Route to edit a comment
@comment_routes.route("/comments/<int:comment_id>/edit", methods=["GET", "POST"])
@login_required
def edit_comment(comment_id):
    comment = Comment.query.get_or_404(comment_id)
    if comment.user_id != current_user.id:
        flash("You do not have permission to edit this comment.", "danger")
        return redirect(url_for("tweet_routes.list_tweets"))

    if request.method == "POST":
        content = request.form.get("content")
        if not content:
            flash("Comment cannot be empty.", "danger")
            return redirect(
                url_for("comment_routes.edit_comment", comment_id=comment_id)
            )
        comment.content = content
        db.session.commit()
        flash("Comment updated successfully!", "success")
        return redirect(url_for("tweet_routes.view_tweet", tweet_id=comment.tweet_id))

    return render_template("edit_comment.html", comment=comment)


# Route to delete a comment
@comment_routes.route("/comments/<int:comment_id>/delete", methods=["POST"])
@login_required
def delete_comment(comment_id):
    comment = Comment.query.get_or_404(comment_id)
    if comment.user_id != current_user.id:
        flash("You do not have permission to delete this comment.", "danger")
        return redirect(url_for("tweet_routes.list_tweets"))

    db.session.delete(comment)
    db.session.commit()
    flash("Comment deleted successfully!", "success")
    return redirect(url_for("tweet_routes.view_tweet", tweet_id=comment.tweet_id))
