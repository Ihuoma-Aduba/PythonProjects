person_1_name = input("What is your name? ")
person_1_wallet = input("How much are you worth? ")

person_2_name = input("What is your name? ")
person_2_wallet = input("How much are you worth? ")

person_3_name = input("What is your name? ")
person_3_wallet = input("How much are you worth? ")

if float(person_1_wallet) > float(person_2_wallet) and float(person_1_wallet) > float(person_3_wallet):
    print(person_1_name + " is the richest")
elif float(person_2_wallet) > float(person_1_wallet) and float(person_2_wallet) > float(person_3_wallet):
    print(person_2_name + " is the wealthiest!")
else: print(person_3_name + " is the wealthiest!")
