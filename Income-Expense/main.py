import csv
from datetime import datetime

FILE_NAME = "expenses.csv"

# Function to add Expense
def add_expenses(amount,category):
    date = datetime.now().strftime("%Y-%m-%d")
    with open(FILE_NAME, "a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([date,amount,category])
    print("Expenses added Succesfully")

# Function to view all Expenses
def view_expenses():
    try:
        with open(FILE_NAME, "r") as file:
            reader = csv.reader(file)
            print("Reader",reader)
            for row in reader:
                print(row)
    except FileNotFoundError:
        print("No File Found")

# Function to Sum the Expenses for Month
def sum_expenses():
    total = 0
    current_month = datetime.now().strftime("%Y-%m")
    print(current_month)
    try:
        with open(FILE_NAME, "r") as file:
            reader = csv.reader(file)
            for row in reader:
                if len(row) < 3:
                    continue
                date,amount,category = row
                print("Date",date)
                if date.startswith(current_month):
                    total += float(amount)
        print(f"Total expenses for current month is {total}")
    except FileNotFoundError:
        print("No expenses found Yet")

# Menu function for User
def menu():
    while True:
        print("\nExpenses Tracker")
        print("1. Add Expenses")
        print("2. View Expenses")
        print("3. Total Expenses")
        print("4. Exit Expenses")

        choice = input("Enter choice: ")

        if choice == "1":
            amount = input("Enter the amount")
            category = input("Enter the category")
            add_expenses(amount=amount,category=category)
        
        elif choice == "2":
            view_expenses()

        elif choice == "3":
            sum_expenses()

        elif choice == "4":
            print("Exiting Bye..")
            break
        else:
            print("Invalid Choice ")

menu()
