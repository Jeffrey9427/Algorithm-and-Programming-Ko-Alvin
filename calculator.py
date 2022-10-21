"Make a calcuation program"

def addition(num1,num2):
    return num1+num2

def substraction(num1,num2):
    return num1-num2

def division(num1,num2):
    return num1/num2

def multiplication(num1,num2):
    return num1*num2

while condition == "Yes":
    num1 = eval(input("Enter number 1: "))
    num2 = eval(input("Enter number 2: "))
    calc = input("Choose a calculation that you want to do (+, -, *, /): ")
    if calc == '+':
        print(f"The addition of the numbers is {addition(num1,num2)}")
    elif calc == '-':
        print(f"The substraction of the numbers is {substraction(num1,num2)}")
    elif calc == '*':
        print(f"The multiplication of the numbers is {multiplication(num1,num2)}")
    else: 
        print(f"The division of the numbers is: {division(num1,num2)}")
    condition = input("Do you want to run the program again (Yes/No)? ")
else: 
    print("The program has stopped")