import re

menu = {"Pizza": 40, "Pasta": 50, "Burger": 60, "Salad": 70, "Coffee": 80}

def add_order(text):
    """Return the price of one order like '3 pizza' or 'pasta'. Returns 0 if invalid."""
    parts = text.strip().split(maxsplit=1)

    if len(parts) == 2 and parts[0].isdigit():
        qty = int(parts[0])
        name = parts[1].strip().title()
    else:
        qty = 1
        name = text.strip().title()

    if name in menu:
        print(f"Order of {qty} x {name} has been added.")
        return menu[name] * qty
    else:
        print(f"Sorry, '{text.strip()}' is not on the menu.")
        return 0

def add_line(line):
    """Handle a full line like '2 coffee and 3 pasta'."""
    items = re.split(r"\s*(?:,|\band\b)\s*", line.strip(), flags=re.IGNORECASE)
    return sum(add_order(item) for item in items if item)

print("Welcome to our restaurant. Here's the menu:")
for item, price in menu.items():
    print(f"{item}: Rs{price}")

total = add_line(input("Enter your first item you want to order = "))

while input("Do you want to order anything else? ").strip().lower() == "yes":
    total += add_line(input("Enter your next item = "))

print(f"The total price to pay is {total}")