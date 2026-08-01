total = 0

while True:
    expense = input("Enter Expense (or type 'done' to finish): ")

    if expense.lower() == "done":
        break

    total = total + float(expense)

print("\nTotal Expense =", total)
