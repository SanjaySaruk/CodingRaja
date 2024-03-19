import json
# File to store budget data
DATA_FILE = "budget_data.json"
# Function to load budget data from file
def load_data():
try:
with open(DATA_FILE, "r") as file:
return json.load(file)
except FileNotFoundError:
return {"income": 0, "expenses": []}
# Function to save budget data to file
def save_data(data):
with open(DATA_FILE, "w") as file:
json.dump(data, file)
# Function to add income
def add_income(data):
income = float(input("Enter income amount: "))
data["income"] += income
print(f"Income of ${income} added successfully.")
save_data(data)
# Function to add expense
def add_expense(data):
category = input("Enter expense category: ")
amount = float(input("Enter expense amount: "))
data["expenses"].append({"category": category, "amount": amount})
print(f"Expense of ${amount} in {category} category added successfully.")
save_data(data)
# Function to calculate remaining budget
def calculate_remaining_budget(data):
total_expenses = sum(expense["amount"] for expense in data["expenses"])
remaining_budget = data["income"] - total_expenses
print(f"Remaining Budget: ${remaining_budget:.2f}")
# Function to analyze expenses
def analyze_expenses(data):
expense_categories = {}
for expense in data["expenses"]:
category = expense["category"]
amount = expense["amount"]
if category in expense_categories:
expense_categories[category] += amount
else:
expense_categories[category] = amount
print("Expense Analysis:")
for category, amount in expense_categories.items():
print(f"{category}: ${amount:.2f}")
# Main function
def main():
print("Welcome to the Budget Tracker!")
budget_data = load_data()
while True:
print("\n===== Menu =====")
print("1. Add Income")
print("2. Add Expense")
print("3. Calculate Remaining Budget")
print("4. Analyze Expenses")
print("5. Exit")
choice = input("Enter your choice (1-5): ")
if choice == "1":
add_income(budget_data)
elif choice == "2":
add_expense(budget_data)
elif choice == "3":
calculate_remaining_budget(budget_data)
elif choice == "4":
analyze_expenses(budget_data)
elif choice == "5":
print("Thank you for using Budget Tracker. Goodbye!")
break
else:
print("Invalid choice. Please enter a number from 1 to 5.")
if __name__ == "__main__":
main() import json
# File to store budget data
DATA_FILE = "budget_data.json"
# Function to load budget data from file
def load_data():
try:
with open(DATA_FILE, "r") as file:
return json.load(file)
except FileNotFoundError:
return {"income": 0, "expenses": []}
# Function to save budget data to file
def save_data(data):
with open(DATA_FILE, "w") as file:
json.dump(data, file)
# Function to add income
def add_income(data):
income = float(input("Enter income amount: "))
data["income"] += income
print(f"Income of ${income} added successfully.")
save_data(data)
# Function to add expense
def add_expense(data):
category = input("Enter expense category: ")
amount = float(input("Enter expense amount: "))
data["expenses"].append({"category": category, "amount": amount})
print(f"Expense of ${amount} in {category} category added successfully.")
save_data(data)
# Function to calculate remaining budget
def calculate_remaining_budget(data):
total_expenses = sum(expense["amount"] for expense in data["expenses"])
remaining_budget = data["income"] - total_expenses
print(f"Remaining Budget: ${remaining_budget:.2f}")
# Function to analyze expenses
def analyze_expenses(data):
expense_categories = {}
for expense in data["expenses"]:
category = expense["category"]
amount = expense["amount"]
if category in expense_categories:
expense_categories[category] += amount
else:
expense_categories[category] = amount
print("Expense Analysis:")
for category, amount in expense_categories.items():
print(f"{category}: ${amount:.2f}")
# Main function
def main():
print("Welcome to the Budget Tracker!")
budget_data = load_data()
while True:
print("\n===== Menu =====")
print("1. Add Income")
print("2. Add Expense")
print("3. Calculate Remaining Budget")
print("4. Analyze Expenses")
print("5. Exit")
choice = input("Enter your choice (1-5): ")
if choice == "1":
add_income(budget_data)
elif choice == "2":
add_expense(budget_data)
elif choice == "3":
calculate_remaining_budget(budget_data)
elif choice == "4":
analyze_expenses(budget_data)
elif choice == "5":
print("Thank you for using Budget Tracker. Goodbye!")
break
else:
print("Invalid choice. Please enter a number from 1 to 5.")
if __name__ == "__main__":
main()
