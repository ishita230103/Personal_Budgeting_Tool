import sqlite3

def create_database():
    conn = sqlite3.connect('budget.db')
    cursor = conn.cursor()
    
    # Create tables for income and expenses
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS income (
            id INTEGER PRIMARY KEY,
            amount REAL,
            source TEXT,
            date TEXT
        )
    ''')
    
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS expenses (
            id INTEGER PRIMARY KEY,
            amount REAL,
            category TEXT,
            date TEXT,
            description TEXT
        )
    ''')
    
    conn.commit()
    conn.close()

create_database()

def add_income(amount, source, date):
    conn = sqlite3.connect('budget.db')
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO income (amount, source, date) 
        VALUES (?, ?, ?)
    ''', (amount, source, date))
    conn.commit()
    conn.close()

def add_expense(amount, category, date, description):
    conn = sqlite3.connect('budget.db')
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO expenses (amount, category, date, description) 
        VALUES (?, ?, ?, ?)
    ''', (amount, category, date, description))
    conn.commit()
    conn.close()

def view_income():
    conn = sqlite3.connect('budget.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM income')
    rows = cursor.fetchall()
    conn.close()
    return rows

def view_expenses():
    conn = sqlite3.connect('budget.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM expenses')
    rows = cursor.fetchall()
    conn.close()
    return rows

def total_income():
    conn = sqlite3.connect('budget.db')
    cursor = conn.cursor()
    cursor.execute('SELECT SUM(amount) FROM income')
    total = cursor.fetchone()[0] or 0
    conn.close()
    return total

def total_expenses():
    conn = sqlite3.connect('budget.db')
    cursor = conn.cursor()
    cursor.execute('SELECT SUM(amount) FROM expenses')
    total = cursor.fetchone()[0] or 0
    conn.close()
    return total

def main():
    create_database()
    
    while True:
        print("\nPersonal Budgeting Tool")
        print("1. Add Income")
        print("2. Add Expense")
        print("3. View Income")
        print("4. View Expenses")
        print("5. Total Income")
        print("6. Total Expenses")
        print("7. Exit")
        
        choice = input("Choose an option: ")
        
        if choice == '1':
            amount = float(input("Enter income amount: "))
            source = input("Enter income source: ")
            date = input("Enter date (YYYY-MM-DD): ")
            add_income(amount, source, date)
        
        elif choice == '2':
            amount = float(input("Enter expense amount: "))
            category = input("Enter expense category: ")
            date = input("Enter date (YYYY-MM-DD): ")
            description = input("Enter description: ")
            add_expense(amount, category, date, description)
        
        elif choice == '3':
            incomes = view_income()
            print("\nIncome Records:")
            for income in incomes:
                print(income)
        
        elif choice == '4':
            expenses = view_expenses()
            print("\nExpense Records:")
            for expense in expenses:
                print(expense)
        
        elif choice == '5':
            print(f"Total Income: ${total_income():.2f}")
        
        elif choice == '6':
            print(f"Total Expenses: ${total_expenses():.2f}")
        
        elif choice == '7':
            print("Goodbye!")
            break
        
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()


