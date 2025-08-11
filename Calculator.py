def addition(a, b):
    return a + b

def substraction(a, b):
    return a - b

def multiplication(a, b):
    return a * b

def division(a, b):
    return a / b

operation = input("Enter the type of operation you wanna do: ")

match (operation):
    case "addition":
        a = input("give me the firts number: ")
        b = input("give me the second number: ")
        print(f"the result is {addition(a,b)}")

    case "substraction":
        a = input("give me the minuend: ")
        b = input("give me the subtrahend: ")
        print(f"the difference is {substraction(a, b)}")

    case _:
        print("None of the operations were specified!")
             