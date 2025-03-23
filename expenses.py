import sqlite3


def add_expense(amount, category, description, date):
    conn = sqlite3.connect("expenses.db")
    cursor = conn.cursor()
    cursor.execute("INSERT INTO expenses (amount, category, description, date) VALUES (?, ?, ?, ?)",
                   (amount, category, description, date))
    conn.commit()
    conn.close()


def view_expenses():
    conn = sqlite3.connect("expenses.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM expenses")
    expenses = cursor.fetchall()
    conn.close()
    return expenses


def delete_expense(expense_id):
    conn = sqlite3.connect("expenses.db")
    cursor = conn.cursor()
    cursor.execute("DELETE FROM expenses WHERE id = ?", (expense_id,))
    conn.commit()
    conn.close()


def get_monthly_summary(month):
    """Calculate the total expenses for a given month (format: YYYY-MM)."""
    conn = sqlite3.connect("expenses.db")
    cursor = conn.cursor()
    cursor.execute("SELECT SUM(amount) FROM expenses WHERE date LIKE ?", (f"{month}%",))
    total = cursor.fetchone()[0]  # Fetch the total sum
    conn.close()
    return total if total else 0.0  # Return 0 if no expenses found
