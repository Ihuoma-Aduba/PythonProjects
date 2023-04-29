list = ["red", "yellow", "blue"]
print(list)
list.insert(2, "pink")
list[1] = "grey"
print(list)

#Tuple

colors = ("blue", "yellow", "red")
print(colors)
#colors.insert(2, black)
#The above code will not work because tuples don't accept the insert function

colors = ("blue", "yellow", "red")
shapes = ("square", "triangle", "circle")
tuple = colors + shapes
print(tuple)