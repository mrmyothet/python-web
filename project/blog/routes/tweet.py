from flask import Blueprint, request, render_template, redirect, url_for, flash
from flask_login import login_required, current_user
from ..models import Tweet, User, db

tweet_routes = Blueprint("tweet_routes", __name__)


@tweet_routes.route("/")
def home():
    return redirect(url_for("tweet_routes.list_tweets"))


# List all tweets
@tweet_routes.route("/tweets", methods=["GET"])
def list_tweets():
    tweets = Tweet.query.order_by(
        Tweet.created_at.desc()
    ).all()  # Show latest tweets first
    return render_template("tweets.html", tweets=tweets)


# Create a new tweet
@tweet_routes.route("/tweets/new", methods=["GET", "POST"])
@login_required
def create_tweet():
    if request.method == "POST":
        content = request.form.get("content")

        # Validate content
        if not content:
            flash("Content is required!", "danger")
            return redirect(url_for("tweet_routes.create_tweet"))

        # Create and save the tweet
        new_tweet = Tweet(
            content=content, user_id=current_user.id
        )  # Use the logged-in user's ID
        db.session.add(new_tweet)
        try:
            db.session.commit()
            flash("Tweet created successfully!", "success")
        except Exception as e:
            db.session.rollback()
            flash("An error occurred. Please try again.", "danger")
            print(str(e))  # For debugging purposes

        return redirect(url_for("tweet_routes.list_tweets"))

    return render_template("create_tweet.html")


# Edit an existing tweet
@tweet_routes.route("/tweets/<int:tweet_id>/edit", methods=["GET", "POST"])
@login_required  # Ensure the user is logged in
def edit_tweet(tweet_id):
    tweet = Tweet.query.get_or_404(tweet_id)

    # Check if the logged-in user owns the tweet
    if tweet.user_id != current_user.id:
        flash("You do not have permission to edit this tweet.", "danger")
        return redirect(url_for("tweet_routes.list_tweets"))

    if request.method == "POST":
        tweet.content = request.form.get("content")

        # Validate content
        if not tweet.content:
            flash("Content is required!", "danger")
            return redirect(url_for("tweet_routes.edit_tweet", tweet_id=tweet_id))

        try:
            db.session.commit()
            flash("Tweet updated successfully!", "success")
        except Exception as e:
            db.session.rollback()
            flash("An error occurred. Please try again.", "danger")
            print(str(e))  # For debugging purposes

        return redirect(url_for("tweet_routes.list_tweets"))

    return render_template("edit_tweet.html", tweet=tweet)


# Delete a tweet
@tweet_routes.route("/tweets/<int:tweet_id>/delete", methods=["POST"])
@login_required  # Ensure the user is logged in
def delete_tweet(tweet_id):
    tweet = Tweet.query.get_or_404(tweet_id)

    # Check if the logged-in user owns the tweet
    if tweet.user_id != current_user.id:
        flash("You do not have permission to delete this tweet.", "danger")
        return redirect(url_for("tweet_routes.list_tweets"))

    try:
        db.session.delete(tweet)
        db.session.commit()
        flash("Tweet deleted successfully!", "success")
    except Exception as e:
        db.session.rollback()
        flash("An error occurred. Please try again.", "danger")
        print(str(e))  # For debugging purposes

    return redirect(url_for("tweet_routes.list_tweets"))


# View a single tweet
@tweet_routes.route("/tweets/<int:tweet_id>", methods=["GET"])
def view_tweet(tweet_id):
    tweet = Tweet.query.get_or_404(tweet_id)
    return render_template("tweet_detail.html", tweet=tweet)
