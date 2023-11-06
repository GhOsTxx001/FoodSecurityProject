import sqlite3

def connect_db():
    return sqlite3.connect('food_security_db.db')

def close_db(conn):
    conn.close()

def distribute_food_weekly():
    conn = connect_db()
    cursor = conn.cursor()

    # Get all users
    cursor.execute("SELECT username, preference FROM users")
    users = cursor.fetchall()

    for user in users:
        username, preference = user
        print(f"Distributing food items for {username}...")

        # Get food items in the user's preferred category
        cursor.execute("SELECT name, quantity FROM food_inventory WHERE category = ?", (preference,))
        food_items = cursor.fetchall()

        # For simplicity, distribute one item from each group
        if food_items:
            food_item, quantity = food_items[0]
            print(f"Allocating {food_item} ({preference}) to {username}")

            # Update the quantity of the food item in the database
            new_quantity = quantity - 1
            cursor.execute("UPDATE food_inventory SET quantity = ? WHERE name = ?", (new_quantity, food_item))
            conn.commit()
        else:
            print(f"No more {preference} available for {username}")

    close_db(conn)

# Run the food distribution function
distribute_food_weekly()