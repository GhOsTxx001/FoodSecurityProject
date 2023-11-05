
import sqlite3

# Connect to the database
conn = sqlite3.connect('./../db/food_insecurity.db')
c = conn.cursor()

# Create the table if it doesn't exist
c.execute('''CREATE TABLE IF NOT EXISTS nutritional_info
             (id INTEGER PRIMARY KEY,
              food_name TEXT,
              calories INTEGER,
              protein INTEGER,
              carbs INTEGER,
              fat INTEGER)''')

# Create
def create_nutritional_info(food_name, calories, protein, carbs, fat):
    c.execute("INSERT INTO nutritional_info (food_name, calories, protein, carbs, fat) VALUES (?, ?, ?, ?, ?)",
              (food_name, calories, protein, carbs, fat))
    conn.commit()

# Read
def read_nutritional_info():
    c.execute("SELECT * FROM nutritional_info")
    rows = c.fetchall()
    for row in rows:
        print(row)

# Update
def update_nutritional_info(id, food_name=None, calories=None, protein=None, carbs=None, fat=None):
    update_dict = {}
    if food_name:
        update_dict['food_name'] = food_name
    if calories:
        update_dict['calories'] = calories
    if protein:
        update_dict['protein'] = protein
    if carbs:
        update_dict['carbs'] = carbs
    if fat:
        update_dict['fat'] = fat
    update_cols = ', '.join([f"{col} = ?" for col in update_dict.keys()])
    update_vals = tuple(update_dict.values())
    c.execute(f"UPDATE nutritional_info SET {update_cols} WHERE id = ?", (*update_vals, id))
    conn.commit()

# Delete
def delete_nutritional_info(id):
    c.execute("DELETE FROM nutritional_info WHERE id = ?", (id,))
    conn.commit()

# Close the connection
conn.close()
