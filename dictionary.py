colors = {"B" : "blue",
          "R" :"red",
          "G" : "green",
          "t" : "green",
}

print(colors.get("B", "stop"))

print(colors.get("b", "stop"))

print(colors.get("t", "stop"))