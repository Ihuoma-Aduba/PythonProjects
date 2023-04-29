from math import*

print("A whole pizza costs 100")
one_pizza_slice = 10

customer_1 = input("What is your name?")
customer_2 = input("What is your name?")
customer_3 = input("What is your name?")

pizza_slice = input("How many slices does the pizza have?")

Jake_slices = input(customer_1 + " How many pizza slices did you eat?")
Tommy_slices = input(customer_2 + " How many pizza slices did you eat?")
Joey_slices = input(customer_3 + " How many pizza slices did you eat?")

Jake_amount = float(Jake_slices) * float(one_pizza_slice)
Tommy_amount = float(Tommy_slices) * float(one_pizza_slice)
Joey_amount = float(Joey_slices) * float(one_pizza_slice)

print(customer_1 + " you ate " + str(Jake_slices) + " slices of pizza, so you will pay $" + str(Jake_amount))
print(customer_2 + " you ate " + str(Tommy_slices) + " slices of pizza, so you will pay $" + str(Tommy_amount))
print(customer_3 + " you ate " + str(Joey_slices) + " slices of pizza, so you will pay $" + str(Joey_amount))

print("Thanks for shopping with us, please do come back later!!!!!")