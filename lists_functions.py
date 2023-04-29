food = ["hamburger", "pizza", "juice", "fries", "sushi"]

prices = [5, 64, 3.92, 7, 29, 4.95, 3.28]

#Add an element to a list
food.insert(2, "spaghetti")

#food.clear()

#Know the number of an element in a list
print(food.index("pizza"))

print(food.index("juice"))

#Add lists to lists
food.extend(prices)

print(food)

#Count the number of times an element appeared in a list
food = ["hamburger", "fries", "sushi", "pizza", "sushi", "hamburger", "juice", "fries", "sushi"]
food.insert(2, "spaghetti")
print(food.count("hamburger"))
print(food.count("spaghetti"))

#Copy lists
copied = food.copy()
number = prices.copy()
print(copied + number)

                                         #OR


copied = food.copy() + prices.copy()
print(copied)