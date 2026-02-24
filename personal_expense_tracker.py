# Personal Expense Tracker
# Created by Vaibhav Kale
# Date : 25 Feb 2026

print("==================== PERSONAL EXPENSE TRACKER ====================")
print()

print("NOTE :-")
print("\n# Enter your current monthly or yearly budget amount (in rupees).""\n# Budget value must not be 0 or fractional (like 1/2 or 3/4).")
print()

budget = float(input("Enter your budget : "))
print()


print("Please specify the amount you spend on each of the following categories (in rupees) :-")
print()

print("- Rent""\n- Groceries""\n- Food""\n- Fuel for Vehicle""\n- Travel""\n- Internet and Phone Bills""\n- Academics""\n- Gym""\n- Health and Medicines""\n- Clothes and Self-Grooming""\n- Entertainment""\n- EMI""\n- Insurance""\n- Miscellaneous")
print()


print("NOTE :-\n\n# Please enter values in numeric format only (Example: 500 or 500.75). Fractions like 1/2 or 3/4 are not supported.\n# Enter 0 if not applicable in amount section.\n# All fields are mandatory.")
print()


categories = ["Rent", "Groceries", "Food", "Fuel for Vehicle", "Travel", "Internet and Phone Bills", "Academics", "Gym", "Health and Medicines", "Clothes and Self-Grooming", "Entertainment", "EMI", "Insurance", "Miscellaneous"]


print("ENTER AMOUNT BELOW :-")
print()


c1 = float(input("Rent : "))
c2 = float(input("Groceries : "))
c3 = float(input("Food : "))
c4 = float(input("Fuel for Vehicle : "))
c5 = float(input("Travel : "))
c6 = float(input("Internet and Phone Bills : "))
c7 = float(input("Academics : "))
c8 = float(input("Gym : "))
c9 = float(input("Health and Medicines : "))
c10 = float(input("Clothes and Self-Grooming : "))
c11 = float(input("Entertainment : "))
c12 = float(input("EMI : "))
c13 = float(input("Insurance : "))
c14 = float(input("Miscellaneous : "))
print()


expense = [c1, c2, c3, c4, c5, c6, c7, c8, c9, c10, c11, c12, c13, c14]


print("==================== TOTAL EXPENDITURE SUMMARY ====================")
print()


total = sum(expense)

print("\nTOTAL EXPENSE : Rs.", total)


max_expense = max(expense)
min_expense = min(expense)


max_index = expense.index(max_expense)
min_index = expense.index(min_expense)


max_category = categories[max_index]
min_category = categories[min_index]


print("\nHIGHEST EXPENSE : Rs.", max_expense)
print("\nHIGHEST EXPENSE CATEGORY :", max_category)


print("\nLOWEST EXPENSE : Rs.", min_expense)
print("\nLOWEST EXPENSE CATEGORY :", min_category)


print("\nAVERAGE EXPENSE : Rs.", (total/14))


remaining = budget - total

print("\nREMAINING BALANCE : Rs.", remaining)


bal_percentage = (remaining / budget) * 100

print("\nREMAINING BALANCE PERCENTAGE :", round(bal_percentage, 2), "%")


print("\n(Negative value means overspending)")