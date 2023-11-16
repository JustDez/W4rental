class Expense:
    def __init__(self, name, amount):
        self.name = name
        self.amount = amount


class Income:
    def __init__(self, name, amount):
        self.name = name
        self.amount = amount


class Property:
    def __init__(self, name, expenses=None, incomes=None):
        self.name = name
        self.expenses = expenses if expenses else []
        self.incomes = incomes if incomes else []
        self.roi = None

    def calculate_roi(self):
        total_expenses = sum(expense.amount for expense in self.expenses)
        total_incomes = sum(income.amount for income in self.incomes)
        self.roi = (total_incomes - total_expenses) / total_expenses * 100 if total_expenses > 0 else 0

    def display_roi(self):
        print(f"ROI for Property {self.name}: {self.roi:.2f}%")
        

class User:
    def __init__(self, name):
        self.name = name
        self.properties = []

    def add_property(self, property):
        self.properties.append(property)


def main():
    users = []

    while True:
        print("\n1. Add User\n2. Add Property\n3. Add Expense\n4. Add Income\n5. Calculate and Display ROI\n6. Exit")
        choice = int(input("Select an option: "))

        if choice == 1:
            user_name = input("Enter user name: ")
            user = User(user_name)
            users.append(user)
            print(f"User {user_name} added.")

        elif choice == 2:
            user_name = input("Enter user name: ")
            property_name = input("Enter property name: ")
            user = next((u for u in users if u.name == user_name), None)
            if user:
                property = Property(property_name)
                user.add_property(property)
                print(f"Property {property_name} added to user {user_name}.")
            else:
                print(f"User {user_name} not found.")

        elif choice == 3:
            user_name = input("Enter user name: ")
            property_name = input("Enter property name: ")
            expense_name = input("Enter expense name: ")
            expense_amount = float(input("Enter expense amount: "))
            user = next((u for u in users if u.name == user_name), None)
            if user:
                property = next((p for p in user.properties if p.name == property_name), None)
                if property:
                    expense = Expense(expense_name, expense_amount)
                    property.expenses.append(expense)
                    print(f"Expense {expense_name} added to property {property_name}.")
                else:
                    print(f"Property {property_name} not found.")
            else:
                print(f"User {user_name} not found.")

        elif choice == 4:
            user_name = input("Enter user name: ")
            property_name = input("Enter property name: ")
            income_name = input("Enter income name: ")
            income_amount = float(input("Enter income amount: "))
            user = next((u for u in users if u.name == user_name), None)
            if user:
                property = next((p for p in user.properties if p.name == property_name), None)
                if property:
                    income = Income(income_name, income_amount)
                    property.incomes.append(income)
                    print(f"Income {income_name} added to property {property_name}.")
                else:
                    print(f"Property {property_name} not found.")
            else:
                print(f"User {user_name} not found.")

        elif choice == 5:
            user_name = input("Enter user name: ")
            property_name = input("Enter property name: ")
            user = next((u for u in users if u.name == user_name), None)
            if user:
                property = next((p for p in user.properties if p.name == property_name), None)
                if property:
                    property.calculate_roi()
                    property.display_roi()
                else:
                    print(f"Property {property_name} not found.")
            else:
                print(f"User {user_name} not found.")

        elif choice == 6:
            print("Exiting program.")
            break

        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
