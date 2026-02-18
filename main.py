import csv
import os

FILE_NAME = "data.csv"


if not os.path.exists(FILE_NAME):
    with open(FILE_NAME, "w", newline="") as file:
        pass


def add_expense():
    date = input("Enter Date (YYYY-MM-DD): ")
    category = input("Enter Category: ")
    amount = input("Enter Amount: ")
    description = input("Enter Description: ")

    with open(FILE_NAME, mode="a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([date, category, amount, description])

    print("✅ Expense Added Successfully!")


def view_expenses():
    try:
        with open(FILE_NAME, mode="r") as file:
            reader = csv.reader(file)
            expenses = list(reader)

            if not expenses:
                print("No expenses found.")
                return

            print("\n-------------------------------------------------------------")
            print(f"{'No':<5}{'Date':<15}{'Category':<15}{'Amount':<10}{'Description':<15}")
            print("-------------------------------------------------------------")

            for i, row in enumerate(expenses, start=1):
                print(f"{i:<5}{row[0]:<15}{row[1]:<15}{row[2]:<10}{row[3]:<15}")

            print("-------------------------------------------------------------")

    except FileNotFoundError:
        print("File not found.")


def delete_expense():
    with open(FILE_NAME, mode="r") as file:
        reader = csv.reader(file)
        expenses = list(reader)

    if not expenses:
        print("No expenses to delete.")
        return

    view_expenses()

    try:
        choice = int(input("Enter expense number to delete: "))
        if 1 <= choice <= len(expenses):
            expenses.pop(choice - 1)

            with open(FILE_NAME, mode="w", newline="") as file:
                writer = csv.writer(file)
                writer.writerows(expenses)

            print("✅ Expense Deleted Successfully!")
        else:
            print("Invalid choice.")

    except ValueError:
        print("Please enter a valid number.")


def monthly_summary():
    month = input("Enter month (MM): ")
    total = 0

    with open(FILE_NAME, mode="r") as file:
        reader = csv.reader(file)

        for row in reader:
            if row[0][5:7] == month:
                total += float(row[2])

    print(f"Total Expense for month {month}: {total}")


def main():
    while True:
        print("\n---- Personal Expense Tracker ----")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Delete Expense")
        print("4. Monthly Summary")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_expense()
        elif choice == "2":
            view_expenses()
        elif choice == "3":
            delete_expense()
        elif choice == "4":
            monthly_summary()
        elif choice == "5":
            print("Exiting...")
            break
        else:
            print("Invalid choice. Try again.")


if __name__ == "__main__":
    main()

