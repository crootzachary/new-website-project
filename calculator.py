from functools import reduce
import math
def addition(*args):
    newList = []
    for i in inputList:
        a = int(i)
        newList.append(a)
    NumbersSum = sum(newList)
    return NumbersSum

def subtraction(*args):
    newList = []
    for i in inputList:
        a = int(i)
        newList.append(a)
    NumbersSub = newList[0] - sum(newList[1:])
    return NumbersSub

def multiplication(*args):
    newList = []
    for i in inputList:
        a = int(i)
        newList.append(a)
    NumbersMult = reduce(lambda x, y: x*y, newList)
    return NumbersMult

def division(*args):
    newList = []
    for i in inputList:
        a = int(i)
        newList.append(a)
    NumbersDiv = reduce(lambda x, y: x/y, newList)
    return NumbersDiv

def natural_logs(*args):
    a = float(input("Input a number: "))
    print(math.log(a))
    print("\nWhen using natural logs, you are inputting the number that e to the x power equals, with the output being x!\n")

def common_logs(*args):
    a = float(input("Input a number: "))
    print(math.log10(a))
    print("\nWhen using common logs, you are inputting the number that 10 to the x power equals, with the output being x!\n")

def custom_logs(*args):
    a = float(input("Input the base: "))
    b = float(input("Input the result: "))
    print(math.log(b, a))
    print("\nWhen using custom logs, you are inputting your designated base to the x power equals your designated result, with the output being x!\n")

while True:
    print("\nPlease enter what you want to calculate\n1 -> Addition\n2 -> Subtraction\n3 -> Multiplication\n4 -> Division\n5 -> Natural Logs\n6 -> Common Logs\n7 -> Custom Logs")

    while True:
        try:
            choice = float(input("Enter: "))
            if 1 <= choice <= 7:
                break
            else:
                print("Invalid input. Please enter a number 1-7")
        except ValueError:
            print("Invalid input. Please enter a number 1-7.")

    if 1 <= choice <= 4:
        print("\nPlease enter your values (separate with comma ex: 1,2,3,4): \n")
        inputList = input().split(",")

        if choice == 1:
            varList = addition(*inputList)
            print("\nThe sum of your inputs is:", varList)
        elif choice == 2:
            varList = subtraction(*inputList)
            print("\nThe difference of your inputs is:", varList)
        elif choice == 3:
            varList = multiplication(*inputList)
            print("\nThe product of your inputs is:", varList)
        elif choice == 4:
            varList = division(*inputList)
            print("\nThe quotient of your inputs is:", varList)
    elif choice == 5:
        natural_logs()
    elif choice == 6:
        common_logs()
    elif choice == 7:
        custom_logs()
    else:
        print("\nPlease enter a number 1-7\n")

    while True:
        try:
            retry = int(input("Use calculator again?\n1 -> Yes\n2 -> No\nEnter: "))
            if retry == 1 or retry == 2:
                break
            else:
                print("Invalid input. Please enter 1 or 2.")
        except ValueError:
            print("Invalid input. Please enter 1 or 2.")

    if retry != 1:
        break

print("Bye!")