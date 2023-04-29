price_of_product_1 = input("What is the price of product?")
Quantity_of_product_1 = input("What is the quantity of the product?")
result_product_1 = float(price_of_product_1) * float(Quantity_of_product_1)
#print(result_product_1)


price_of_product_2 = input("What is the price of product?")
Quantity_of_product_2 = input("What is the quantity of the product?")
result_product_2 = float(price_of_product_2) * float(Quantity_of_product_2)
#print(result_product_2)


price_of_product_3 = input("What is the price of product?")
Quantity_of_product_3 = input("What is the quantity of the product?")
result_product_3 = float(price_of_product_3) * float(Quantity_of_product_3)
#print(result_product_3)


#If we just multiply the price by the quantity it is going to give an error because by default python generates a string as an answer
#result_product_1 = price_of_product_1 * Quantity_of_product_1



result = result_product_1 + result_product_2 + result_product_3

#print(result)

print("The total amount is " + str(result))