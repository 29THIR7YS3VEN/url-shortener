from cs50 import SQL
from flask import Flask, flash, jsonify, redirect, render_template, request, session, url_for
from db import *

app = Flask(__name__)
db = SQL("sqlite:///main.db")

dbinit()

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "GET":
        return render_template("index.html")
    else:
        destination = request.form.get("destination")
        custom = request.form.get("custom")

        if not custom:
            db.execute(
                "INSERT INTO links (_destination) VALUES (:d)", d=destination)
            link = db.execute(
                "SELECT * FROM links WHERE _destination == :destination", destination=destination)
            db.execute("UPDATE links WHERE _destination == :d SET _path = :p",
                       d=link[0]["_destination"], p=link[0]["id"])
            return render_template("complete.html", link=link)
        else:
            check = db.execute(
                "SELECT * FROM links WHERE _path == :p", p=custom)
            if check.length != 0:
                flash(
                    "A link with that name already exists. Please try a different one.")
                return redirect("/")
            else:
                db.execute(
                    "INSERT INTO links (_destination, _path) VALUES (:d, :p)", d=destination, p=custom)
                link = db.execute(
                    "SELECT * FROM links WHERE _destination == :destination", destination=destination)
                return render_template("complete.html", link=link)
