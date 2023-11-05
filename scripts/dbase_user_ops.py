import sqlite3
from werkzeug.security import generate_password_hash

def connect_db():
    return sqlite3.connect('./../db/food_security_db.db')

def close_db(conn):
    conn.close()

def insert_user(username, password):
    hashed_password = generate_password_hash(password)
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO users (username, password) VALUES (?, ?)", (username, password))
    conn.commit()
    close_db(conn)

def query_users():
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users")
    rows = cursor.fetchall()
    close_db(conn)
    return rows

def update_user(user_id, username, password):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("UPDATE users SET username = ?, password = ? WHERE user_id = ?", (username, password, user_id))
    conn.commit()
    close_db(conn)

def delete_user(user_id):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM users WHERE user_id = ?", (user_id,))
    conn.commit()
    close_db(conn)

