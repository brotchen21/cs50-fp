import os
from flask import Flask, render_template, request, redirect, flash, url_for
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL', 'sqlite:///database.db')
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"

db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    username = db.Column(db.String(20), unique = True, nullable = False)
    hash = db.Column(db.String(25), nullable = False)

#Ensure responses aren't cached
@app.after_request
def after_request(response):
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response
@app.route("/")
def index():
    return render_template("index.html")


@app.route("/register", methods = ["GET", "POST"])
def register():
    if request.method == "POST":
        username = request.form.get["username"]
        password = request.form.get["password"]
        confirm_password = request.form.get["confirmPassword"]

        #Check if passwords match
        if password != confirm_password:
            flash("Passwords do not match", "danger")
            return render_template("reg.html")
        
        #If user is already taken
        existing_user = User.query.filter_by(username = username).first()
        if existing_user:
            flash("Username already taken", "danger")
            return render_template("reg.html")
        
        #Create user with hashed password
        hashed_password = generate_password_hash(password)
        new_user = User(username = username, password = hashed_password)

        #Add user
        db.session.add(new_user)
        db.session.commit()

        return redirect(url_for("login"))
    return render_template("reg.html")

@app.route("/login")
def login():
    return render_template("login.html")


if __name__ == "__main__":
    app.run(debug=True) 