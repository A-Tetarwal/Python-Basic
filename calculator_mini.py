check = True

while True:
    if check:
        print("calculator for two numbers")
        add = "+"
        multiply = "*"
        divide = "/"
        subtract = "-"
        remainder = "remainder"
        print("------------------")

    entered_value = input("दो नंबर के बीच में कौन सा operation करना है, \n+, -, *, /, remainder, exit\n")
    print("------------------")

    if entered_value == "exit":
        print("Exiting the calculator. Goodbye!")
        break

    n1 = input("enter number 1: ")
    n2 = input("enter number 2: ")

    if entered_value == "+":
        print(int(n1) + int(n2))
    elif entered_value == "-":
        print(int(n1) - int(n2))
    elif entered_value == "*":
        print(int(n1) * int(n2))
    elif entered_value == "/":
        print(int(n1) / int(n2))
    elif entered_value == "remainder":
        print("remainder on dividing n1/n2 is: ", int(n1) % int(n2))
    else:
        print("Invalid operation. Please try again.")

    print("------------------")

    # Resetting the check to control the welcome message display
    check = False
