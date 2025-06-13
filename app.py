from flask import Flask, request, jsonify, render_template
import sqlite3

app = Flask(__name__)

# Function to connect to the SQLite database
def get_db():
    conn = sqlite3.connect('expenses.db')
    conn.row_factory = sqlite3.Row  # To return rows as dictionaries
    return conn

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)

@app.route('/add-expense', methods=['POST'])
def add_expense():
    description = request.form['description']
    amount = request.form['amount']
    conn = get_db()
    conn.execute("INSERT INTO expenses (description, amount) VALUES (?, ?)", (description, amount))
    conn.commit()
    return jsonify({"message": "Expense added successfully!"}), 201

@app.route('/expenses', methods=['GET'])
def get_expenses():
    conn = get_db()
    cur = conn.cursor()
    cur.execute("SELECT * FROM expenses ORDER BY created_at DESC")
    expenses = cur.fetchall()
    return jsonify([dict(expense) for expense in expenses])  # Converts rows to dictionaries

@app.route('/delete-expense/<int:id>', methods=['DELETE'])
def delete_expense(id):
    conn = get_db()
    conn.execute("DELETE FROM expenses WHERE id = ?", (id,))
    conn.commit()
    return jsonify({"message": f"Expense {id} deleted successfully!"}), 200

