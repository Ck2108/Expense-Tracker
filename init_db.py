import sqlite3

conn = sqlite3.connect('expenses.db')
c = conn.cursor()

# Create the expenses table
c.execute('''CREATE TABLE expenses
             (id INTEGER PRIMARY KEY AUTOINCREMENT,
              description TEXT NOT NULL,
              amount REAL NOT NULL,
              created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP)''')

conn.commit()
conn.close()

print("Database initialized!")

