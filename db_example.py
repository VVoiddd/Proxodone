import sqlite3

# Step 1: Connect to the SQLite database
conn = sqlite3.connect('proxodone.db')

# Step 2: Create a cursor object to execute SQL queries
cursor = conn.cursor()

# Step 3: Create a table to store data
cursor.execute('''
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY,
        username TEXT NOT NULL,
        email TEXT NOT NULL
    )
''')

# Step 4: Define functions to interact with the database

def add_user(username, email):
    cursor.execute('''
        INSERT INTO users (username, email)
        VALUES (?, ?)
    ''', (username, email))
    conn.commit()
    print("User added successfully!")

def get_users():
    cursor.execute('''
        SELECT * FROM users
    ''')
    users = cursor.fetchall()
    return users

# Step 5: Test the functions
if __name__ == "__main__":
    # Adding users
    add_user('john_doe', 'john@example.com')
    add_user('jane_smith', 'jane@example.com')

    # Getting all users
    all_users = get_users()
    print("All Users:")
    for user in all_users:
        print(user)

# Step 6: Close the cursor and connection
cursor.close()
conn.close()
