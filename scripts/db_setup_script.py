import sqlite3

# Establish a connection to the SQLite database file (create one if it doesn't exist)
conn = sqlite3.connect('./../db/food_security_db.db')  # Replace 'food_security_db.db' with your desired database name

# Create a cursor object to execute SQL commands
cursor = conn.cursor()

# SQL statements to create the tables
create_users_table = '''
CREATE TABLE IF NOT EXISTS users (
    user_id INTEGER PRIMARY KEY,
    username TEXT,
    password TEXT
    -- Additional columns
);
'''

create_food_inventory_table = '''
CREATE TABLE IF NOT EXISTS food_inventory (
    food_id INTEGER PRIMARY KEY,
    food_name TEXT,
    quantity INTEGER,
    location TEXT,
    expiry_date DATE
    -- Additional columns
);
'''

create_nutritional_info_table = '''
CREATE TABLE IF NOT EXISTS nutritional_info (
    food_id INTEGER,
    calories REAL,
    protein REAL,
    carbs REAL,
    fat REAL,
    FOREIGN KEY (food_id) REFERENCES food_inventory(food_id)
    -- Additional columns
);
'''

# Execute SQL commands to create the tables
cursor.execute(create_users_table)
cursor.execute(create_food_inventory_table)
cursor.execute(create_nutritional_info_table)

# Commit changes and close the connection
conn.commit()
conn.close()
