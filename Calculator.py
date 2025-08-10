def addition(a, b):
    return a + b

operation = input("Enter the type of operation you wanna do: ")

match (operation):
    case "addition":
        a = input("give me the firts number: ")
        b = input("give me the second number: ")
        print(f"the result is {addition(a,b)}")    