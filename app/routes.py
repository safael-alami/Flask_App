from flask import Blueprint, render_template, request, redirect, url_for
from app.db import mysql


main = Blueprint("main", __name__)


@main.route("/")
def index():

    cursor = mysql.connection.cursor()
    cursor.execute("SELECT * FROM users;")
    users = cursor.fetchall()
    cursor.close()

    return render_template("index.html", users=users)


@main.route("/add_user", methods=["POST"])
def add_user():
    username = request.form["username"]
    email = request.form["email"]

   
    cursor = mysql.connection.cursor()
    cursor.execute("INSERT INTO users (username, email) VALUES (%s, %s)", (username, email))
    mysql.connection.commit()
    cursor.close()

    return redirect(url_for("main.index"))


@main.route("/delete_user/<int:user_id>")
def delete_user(user_id):
    cursor = mysql.connection.cursor()
    cursor.execute("DELETE FROM users WHERE id = %s", (user_id,))
    mysql.connection.commit()
    cursor.close()

    return redirect(url_for("main.index"))
