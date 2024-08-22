import os
import sqlite3
import uuid
from flask import Flask, render_template, request, redirect, session, flash, url_for
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)
app.secret_key = 'guy75dt645dfytgus'

def get_db_connection():
    conn = sqlite3.connect('database.db')
    conn.row_factory = sqlite3.Row
    return conn



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


@app.route("/reg.html", methods = ["GET", "POST"])
def register():
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")
        confirm_password = request.form.get("confirmPassword")

        #Check if passwords match
        if password != confirm_password:
            flash("Passwords do not match", "danger")
            return render_template("reg.html")
        
        #If user is already taken
        conn = get_db_connection()
        existing_user = conn.execute("SELECT * FROM users WHERE username = ?", (username,)).fetchone()
        if existing_user:
            flash("Username already taken", "danger")
            conn.close()
            return render_template("reg.html")
        
        #Create user with hashed password
        hashed_password = generate_password_hash(password)
        conn.execute("INSERT INTO users (username, hash) VALUES (?, ?)", (username, hashed_password))
        conn.commit()
        conn.close()

        return redirect("login.html")
    return render_template("reg.html")

@app.route("/login.html", methods=["GET", "POST"])
def login():
    session.clear()
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")
        print(f"Username: {username}, password: {password}")

        if not username:
            flash("Must provide username", "danger")
            return render_template("login.html")
        elif not password:
            flash("Must provide password", "danger")
            return render_template("login.html")   

        conn = get_db_connection()
        cursor = conn.execute("SELECT * FROM users WHERE username = ?", (username,))
        user = cursor.fetchone()
        conn.close()

        if user: 
            print(f"User found: {user}")
        else: 
            print("No user found")
        #Ensure username and password is correct
        if user is None or not check_password_hash(user['hash'], password):
            flash("Invalid username/password", "danger")
            return render_template("login.html")
        
        #Log in
        session["user_id"] = user["id"]
        flash("Logged in successfully", "success")
        return redirect("/")
    else:
        return render_template("login.html")
    
@app.route("/webOrder.html", methods=["GET", "POST"])
def webOrder():
    return render_template("webOrder.html")

@app.route("/thuongHieu.html", methods=["GET", "POST"])
def thuongHieu():
    return render_template("thuongHieu.html")

@app.route("/caphe.html", methods =["GET", "POST"])
def caphe():
    return render_template("caphe.html")

@app.route("/tra.html", methods =["GET", "POST"])
def tra():
    return render_template("tra.html")

@app.route("/freeze.html", methods =["GET", "POST"])
def freeze():
    return render_template("freeze.html")

@app.route("/nguyenban.html", methods =["GET", "POST"])
def nguyenban():
    return render_template("nguyenban.html")

@app.route("/dacbiet.html", methods =["GET", "POST"])
def dacbiet():
    return render_template("dacbiet.html")

@app.route("/khac.html", methods =["GET", "POST"])
def khac():
    return render_template("khac.html")

@app.route("/add_to_cart/<int:product_id>", methods= ["POST"])
def add_to_cart(product_id):
    if "session_id" not in session:
        session["session_id"] = str(uuid.uuid4())
    session_id = session["session_id"]

    conn = get_db_connection()
    cart_item = conn.execute("SELECT * FROM cartItem WHERE session_id = ? AND product_id = ?", (session_id, product_id)).fetchone()
    if cart_item:
        #If item already exists
        conn.execute("UPDATE cartItem SET quantity = quantity + 1 WHERE id = ?", (cart_item["id"],))
    else:
        conn.execute("INSERT INTO cartItem (product_id, quantity, session_id) VALUES (?, ?, ?)", (product_id, 1, session_id))
    
    conn.commit()
    conn.close()
    flash("Item added to cart", "success")
    return redirect(url_for('webOrder'))
    return jsonify(success=True)


@app.route("/cart.html", methods= ["GET"])
def cart():
    if "session_id" not in session:
        return render_template("cart.html", cart_items=[], total_price= 0)
    session_id = session["session_id"]

    conn = get_db_connection()
    cart_items = conn.execute("SELECT product.name, product.price, cartItem.quantity FROM cartItem JOIN product ON cartItem.product_id = product.id WHERE cartItem.session_id = ?", (session_id,)).fetchall()

    total_price = sum(item["price"] * item["quantity"] for item in cart_items)
    conn.close()

    return render_template("cart.html", cart_items=cart_items, total_price=total_price)


if __name__ == "__main__":
    app.run(debug=True) 