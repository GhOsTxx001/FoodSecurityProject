import sqlite3
#checking food availability
def connect_db():
    return sqlite3.connect('food_security_db.db')

def close_db(conn):
    conn.close()

def check_availability(food_item, quantity):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("SELECT quantity FROM food_inventory WHERE name = ?", (food_item,))
    result = cursor.fetchone()
    close_db(conn)
    if result is not None and result[0] >= quantity:
        return True
    return False