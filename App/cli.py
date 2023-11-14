from getpass import getpass
import sqlite3
from werkzeug.security import generate_password_hash, check_password_hash
import random

# Connect to the SQLite database
#for the admin to be able to do his thing from the cli(secret admin login @option 10 in the menu)
conn = sqlite3.connect('./food_security_db.db')
cursor = conn.cursor()

def sign_up():
    conn = sqlite3.connect('./food_security_db.db')
    cursor = conn.cursor()
    username = input("Enter your username: ")
    password = getpass("Enter your password: ")
    hashed_password = generate_password_hash(password)
    cursor.execute("INSERT INTO users (username, password) VALUES (?, ?)", (username, hashed_password))
    conn.commit()
    conn.close()
    print("User created successfully")

def sign_in():
    conn = sqlite3.connect('./food_security_db.db')
    cursor = conn.cursor()
    username = input("Enter your username: ")
    password = getpass("Enter your password: ")
    cursor.execute("SELECT password FROM users WHERE username = ?", (username,))
    result = cursor.fetchone()
    conn.close()
    if result and check_password_hash(result[0], password):
        print("Logged in successfully")
    else:
        print("Login failed. Invalid credentials.")

def view_users():
    conn = sqlite3.connect('./food_security_db.db')
    cursor = conn.cursor()
    cursor.execute("SELECT username FROM users")
    rows = cursor.fetchall()
    for row in rows:
        print(row[0]) #to only fetch the first element
    conn.close()

def add_food_inventory():
    conn = sqlite3.connect('./food_security_db.db')
    cursor = conn.cursor()
    food_name = input("Enter food name: ")
    quantity = int(input("Enter quantity: "))
    location = input("Enter location: ")
    expiry_date = input("Enter expiry date (YYYY-MM-DD): ")
    cursor.execute("INSERT INTO food_inventory (food_name, quantity, location, expiry_date) VALUES (?, ?, ?, ?)", (food_name, quantity, location, expiry_date))
    conn.commit()
    conn.close()
    print("Food inventory added successfully")

def add_nutritional_info():
    conn = sqlite3.connect('./food_security_db.db')
    cursor = conn.cursor()
    food_id = int(input("Enter food id: "))
    calories = float(input("Enter calories: "))
    protein = float(input("Enter protein: "))
    carbs = float(input("Enter carbs: "))
    fat = float(input("Enter fat: "))
    cursor.execute("INSERT INTO nutritional_info (food_id, calories, protein, carbs, fat) VALUES (?, ?, ?, ?, ?)", (food_id, calories, protein, carbs, fat))
    conn.commit()
    conn.close()
    print("Nutritional info added successfully")

def view_food_inventory():
    conn = sqlite3.connect('./food_security_db.db')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM food_inventory")
    rows = cursor.fetchall()
    for row in rows:
        print(row)
    conn.close()

def view_nutritional_info():
    conn = sqlite3.connect('./food_security_db.db')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM nutritional_info")
    rows = cursor.fetchall()
    for row in rows:
        print(row)
    conn.close()


def distribute_food():
    cursor.execute("SELECT user_id FROM users")
    users = cursor.fetchall()

    # Get all food_ids from the inventory
    cursor.execute("SELECT food_id FROM food_inventory WHERE quantity > 0")
    all_food_ids = [row[0] for row in cursor.fetchall()]

    for user in users:
        # Select 3 random food_ids
        food_ids = random.sample(all_food_ids, min(3, len(all_food_ids)))
        quantity = 1
        distribution_date = datetime.now().strftime('%Y-%m-%d')

        for food_id in food_ids:
            # Check if there's enough quantity in the inventory
            cursor.execute("SELECT quantity FROM food_inventory WHERE food_id = ?", (food_id,))
            inventory_quantity = cursor.fetchone()[0]
            if inventory_quantity >= quantity:
                # Deduct the distributed food from the inventory
                cursor.execute("UPDATE food_inventory SET quantity = quantity - ? WHERE food_id = ?", (quantity, food_id))

                # Update the user's record with the distributed food information
                cursor.execute("INSERT INTO food_distribution (user_id, food_id, quantity, distribution_date) VALUES (?, ?, ?, ?)", (user[0], food_id, quantity, distribution_date))

    conn.commit()


# Main loop for user interaction
while True:
    print("Welcome to the Food Security Project")
    print("1. Sign In")
    print("2. Sign Up")
    print("3. View Users")
    print("4. View Food Inventory")
    print("5. View Nutritional Info")
    print("6. Exit")
    print("\n")

    choice = input("Enter your choice: ")

    if choice == '1':
        sign_in()
    elif choice == '2':
        sign_up()
    elif choice == '3':
        view_users()
    elif choice == '4':
        view_food_inventory()
    elif choice == '5':
        view_nutritional_info()
    elif choice == '6':
        print("Goodbye!")
        break
    elif choice == '10':  # Hidden admin sign-in option
        admin_username = input("Enter admin username: ")
        admin_password = getpass("Enter admin password: ")
        cursor.execute("SELECT password FROM users WHERE username = ?", (admin_username,))
        result = cursor.fetchone()
        if result and check_password_hash(result[0], admin_password):
            admin_choice = input("1. Add Food Inventory\n2. Add Nutritional Info\nEnter choice: ")
            if admin_choice == '1':
                add_food_inventory()
            elif admin_choice == '2':
                add_nutritional_info()
            else:
                print("Invalid choice")
        else:
            print("Admin authentication failed")
    else:
        print("Invalid choice. Please enter a valid option.")


#to automate food distribution to weekly basis

from apscheduler.schedulers.background import BackgroundScheduler

scheduler = BackgroundScheduler()
scheduler.add_job(distribute_food, 'interval', weeks=1)
scheduler.start()