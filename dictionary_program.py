# Program demonstrating a dictionary of items

# Create a dictionary of items with their prices
items = {
    "apple": 1.50,
    "banana": 0.75,
    "orange": 2.00,
    "grape": 3.25,
    "mango": 4.00
}

print("Welcome to the Items Dictionary Program!")
print("Here is the list of items and their prices:")
print("-" * 40)

# Iterate through the dictionary and print each item
for item, price in items.items():
    print(f"{item.capitalize()}: ${price:.2f}")

print("-" * 40)
print("Total number of items:", len(items))

# Example of accessing a specific item
print(f"\nPrice of apple: ${items['apple']:.2f}")

# Example of adding a new item
items["pineapple"] = 3.50
print("Added pineapple: $3.50")
print("Updated total items:", len(items))