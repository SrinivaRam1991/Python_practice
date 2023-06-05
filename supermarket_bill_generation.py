# Define a dictionary of products and their prices
products = {'Salt': 10.00, 'Sugar': 50.00, 'Tooth paste': 20.00, 'oats': 200.00}

# Initialize an empty list to store the user's purchases
purchases = []
customer_name = input("Enter your Name:")
Address = input("Enter your address:")
# Loop through the products dictionary and prompt the user to enter a quantity for each product
for product, price in products.items():
    quantity = input(f"How many {product}s would you like to purchase? ")
    if quantity != "":
        purchases.append((product, int(quantity)))
        # Calculate the total cost of the user's purchases
total_cost = sum([quantity * products[product] for product, quantity in purchases])
# Print the bill

print("------------------------------------BILL---------------------------------------------------------------")
print(customer_name)
print(Address)
for product, quantity in purchases:
    print(f"{product} x {quantity}: ${products[product] * quantity}")
print("-------------------------------------------------------------------------------------------------------")
print(f"Total cost: ${total_cost}")
print("----------------------------Thanks For Visiting--------------------------------------------------------")