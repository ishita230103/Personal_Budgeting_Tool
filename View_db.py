import sqlite3

def view_data():
    conn = sqlite3.connect('budget.db')
    cursor = conn.cursor()
    
    # View Income
    print("Income:")
    cursor.execute('SELECT * FROM income')
    for row in cursor.fetchall():
        print(row)

    # View Expenses
    print("\nExpenses:")
    cursor.execute('SELECT * FROM expenses')
    for row in cursor.fetchall():
        print(row)

    conn.close()

if __name__ == "__main__":
    view_data()
