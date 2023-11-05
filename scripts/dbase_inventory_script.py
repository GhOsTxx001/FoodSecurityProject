import sqlite3

def connect_db():
    return sqlite3.connect('./../db/food_security_db.db')

def close_db(conn):
    conn.close()

# Connect to the database and create the table
conn = connect_db()
conn.execute('''CREATE TABLE IF NOT EXISTS food_inventory
             (id INTEGER PRIMARY KEY AUTOINCREMENT,
             name TEXT NOT NULL,
             quantity INTEGER NOT NULL,
             unit TEXT NOT NULL);''')
conn.commit()
close_db(conn)

# Create
def add_food_item(name, quantity, unit):
    conn = connect_db()
    conn.execute("INSERT INTO food_inventory (name, quantity, unit) VALUES (?, ?, ?)", (name, quantity, unit))
    conn.commit()
    close_db(conn)

# Read
def get_food_item(id):
    conn = connect_db()
    cursor = conn.execute("SELECT * FROM food_inventory WHERE id=?", (id,))
    result = cursor.fetchone()
    close_db(conn)
    return result

def get_all_food_items():
    conn = connect_db()
    cursor = conn.execute("SELECT * FROM food_inventory")
    result = cursor.fetchall()
    close_db(conn)
    return result

# Update
def update_food_item(id, name, quantity, unit):
    conn = connect_db()
    conn.execute("UPDATE food_inventory SET name=?, quantity=?, unit=? WHERE id=?", (name, quantity, unit, id))
    conn.commit()
    close_db(conn)

# Delete
def delete_food_item(id):
    conn = connect_db()
    conn.execute("DELETE FROM food_inventory WHERE id=?", (id,))
    conn.commit()
    close_db(conn)