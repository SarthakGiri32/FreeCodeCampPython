import math
from itertools import zip_longest


class Category:
    def __init__(self, name):
        self.name = name
        self.ledger = []

    def deposit(self, amount, description=""):
        self.ledger.append({"amount": amount, "description": description})

    def withdraw(self, amount, description=""):
        if self.check_funds(amount):
            self.ledger.append({"amount": -amount, "description": description})
            return True
        else:
            return False

    def get_balance(self):
        return sum([entry["amount"] for entry in self.ledger])

    def transfer(self, amount, category):
        if self.check_funds(amount):
            self.withdraw(amount, f"Transfer to {category.name}")
            category.deposit(amount, f"Transfer from {self.name}")
            return True
        else:
            return False

    def check_funds(self, amount):
        if amount > self.get_balance():
            return False
        else:
            return True

    def __str__(self):
        display_string = self.name.center(30, "*") + "\n"
        for entry in self.ledger:
            amount_str = f"{entry['amount']:.2f}"[:7]
            display_string += f"{entry['description'][:23]:23}{' ' * (7 - len(amount_str))}{amount_str}\n"
        display_string += f"Total: {self.get_balance():.2f}"
        return display_string


def create_spend_chart(categories: list[Category]):
    expense_per_category = {}
    total_expenses = 0

    for category in categories:
        expense_per_category[category.name] = -sum([entry["amount"] for entry in category.ledger if entry["amount"] < 0])
        total_expenses += expense_per_category[category.name]

    horizontal_line = "    -"
    for category_expense in expense_per_category:
        expense_per_category[category_expense] = math.floor(((expense_per_category[category_expense] / total_expenses) * 100) / 10) * 10
        horizontal_line += "---"

    chart = "Percentage spent by category\n"
    for percentage in range(100, -1, -10):
        single_graph_line = f"{percentage:>3}| "
        for category_expense in expense_per_category:
            single_graph_line += "   " if expense_per_category[category_expense] < percentage else "o  "
        chart += single_graph_line + "\n"
    chart += horizontal_line + "\n"

    x_axis_titles = ""
    category_names = [category.name for category in categories]
    for letters in zip_longest(*category_names, fillvalue=" "):
        x_axis_titles += "     " + "  ".join(letters) + "  " + "\n"
    chart += x_axis_titles.rstrip("\n")

    return chart


if __name__ == "__main__":
    food = Category("Food")
    food.deposit(1000, "initial deposit")
    food.withdraw(10.15, "groceries")
    food.withdraw(15.89, "restaurant and more food for dessert")
    clothing = Category('Clothing')
    food.transfer(283.44, clothing)
    clothing.withdraw(59.57, "yellow t-shirt")
    print(food)
    print(clothing)

    print(create_spend_chart([food, clothing]), end='')
