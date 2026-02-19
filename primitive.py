# The business name (STRING)
business_name = "Faidat's Snack Shop"

# Starting money (NUMBER)
balance = 5000

# Is the shop open? (BOOLEAN)
is_open = True

print("Welcome to", business_name)
print("Shop open:", is_open)

# A customer places an order
customer_name = "Aisha"
order_price = 1500

print(customer_name, "placed an order worth", order_price)

# Update balance after payment
balance = balance + order_price
print("New balance after payment:", balance)

# Cost of making the snacks
ingredients_cost = 600

# Subtract expenses
balance = balance - ingredients_cost
print("Balance after buying ingredients:", balance)

# Create a message combining strings and numbers
summary = customer_name + " bought snacks. Final balance is " + str(balance)
print(summary)

# Change shop status at the end of the day
is_open = False
print("Shop open:", is_open)
