# Define the Menu of Restaurant 
menu = {
    'Pizza': 40,
    'Salad': 50,
    'Apple': 60,
    'Curry': 70,
    'Lemonade': 10,
    'Samosas': 20,
    'Chicken': 150,
}

# Greet the customer
print("Welcome to Coding Cafe Restaurant!")
print("Menu:")
for item, price in menu.items():
    print(f"{item}: BDT{price}")

order_total = 0

# Ask for the first item
item_1 = input("Enter the name of the item you want to order: ")
if item_1 in menu:
    order_total += menu[item_1]
    print(f"Your item '{item_1}' has been added to your order.")
else:
    print(f"Sorry, '{item_1}' is not currently available!")

# Ask if they want to add another item
another_order = input("Do you want to add another item? (Yes/No): ").strip().lower()
# .strip() removes any extra spaces at the beginning or end
# .lower() converts the input to lowercase, so 'YES', 'yes', or 'Yes' are treated the same
if another_order == "yes":
    item_2 = input("Enter the name of the second item you want to order: ")
    if item_2 in menu:
        order_total += menu[item_2]
        print(f"Your item '{item_2}' has been added to your order.")
    else:
        print(f"Sorry, '{item_2}' is not currently available!")

# Display the total bill
print(f"Your total bill is BDT{order_total}.")
# Project 2 - MD Arafat Koyes

