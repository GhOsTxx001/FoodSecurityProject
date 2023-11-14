from flask import Flask, request
import sqlite3
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)

@app.route('/signup', methods=['POST'])
def signup():
    conn = sqlite3.connect('./food_security_db.db')
    cursor = conn.cursor()
    username = request.form['username']
    password = request.form['password']
    hashed_password = generate_password_hash(password)
    cursor.execute("INSERT INTO users (username, password) VALUES (?, ?)", (username, hashed_password))
    conn.commit()
    conn.close()
    return "User created successfully"

@app.route('/login', methods=['POST'])
def login():
    conn = sqlite3.connect('./food_security_db.db')
    cursor = conn.cursor()
    username = request.form['username']
    password = request.form['password']
    cursor.execute("SELECT password FROM users WHERE username = ?", (username,))
    result = cursor.fetchone()
    conn.close()
    if result and check_password_hash(result[0], password):
        return "Logged in successfully"
    else:
        return "Login failed. Invalid credentials."

@app.route('/add_food_inventory', methods=['POST'])
def add_food_inventory():
    conn = sqlite3.connect('./food_security_db.db')
    cursor = conn.cursor()
    food_name = request.form['food_name']
    quantity = request.form['quantity']
    location = request.form['location']
    expiry_date = request.form['expiry_date']
    cursor.execute("INSERT INTO food_inventory (food_name, quantity, location, expiry_date) VALUES (?, ?, ?, ?)", (food_name, quantity, location, expiry_date))
    conn.commit()
    conn.close()
    return "Food inventory added successfully"

@app.route('/add_nutritional_info', methods=['POST'])
def add_nutritional_info():
    conn = sqlite3.connect('./food_security_db.db')
    cursor = conn.cursor()
    food_id = request.form['food_id']
    calories = request.form['calories']
    protein = request.form['protein']
    carbs = request.form['carbs']
    fat = request.form['fat']
    cursor.execute("INSERT INTO nutritional_info (food_id, calories, protein, carbs, fat) VALUES (?, ?, ?, ?, ?)", (food_id, calories, protein, carbs, fat))
    conn.commit()
    conn.close()
    return "Nutritional info added successfully"

if __name__ == "__main__":
    app.run(debug=True)