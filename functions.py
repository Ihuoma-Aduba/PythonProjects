#def love (name):
#    print ("I love " + name)
#love("pizza.")


def store_man_1(store_guy, name, more):
    name = input(store_guy + " Hello, What is your name?")
    more = input(store_guy + " Okay" + name + ". How can I help you?")
    print(store_guy + " Okay, please I will require your answers on the questions now")

def customer(food, drink, dessert, table):
    food = input("What would you like to eat?")
    drink = input("What would you like to drink?")
    dessert = input("What dessert will you have?")
    table = input("How many tables are you making reservations for?")

def store_man_2 (name_1):
    print(name_1 + "Okay your order is being processed, please sit and wait. Thank you!")

store_man_1("Cashier:", "name", "more")
customer("food", "drink", "dessert", "table")
store_man_2("Cashier: ")