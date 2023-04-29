def question_1():
    name = "Host: "
    rule = input(name + "You are required to answer all the questions, do you understand? ").lower()
    if rule != "yes":
        print("Oh, you can't go further, read the rules again!")
    else: print("Let's begin! \nQuestion 1")
    Q1 = input("Do you want to go to school in the USA? ").lower()
    if Q1 != "yes":
        print("Where do you wish to school then? ")
    else: print("Great!")
    Q2 = input("Can you afford to pay high tuition fees? ").lower()
    if Q2 != "yes":
        print("Okay, too bad, but I understand, we could find you some scholarships or financial aid.")
    else: print("Wow!, you are really lucky!")
    Q3 = input("Are you above 18 years of age? ").lower()
    if Q3 != "yes":
        print("Oh no! you'll have to try when you're up to 18.").lower()
    else: print("Good! Let's proceed with finding the perfect school for you.")
question_1()
