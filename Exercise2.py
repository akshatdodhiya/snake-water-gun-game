# Exercise 2 - Faulty Calculator

operator = input("Enter the operator you want to use ")
num1 = int(input("Enter the first number "))
num2 = int(input("Enter the second number "))

if operator=="*" and num1==45 or num1==3 and num2==3 or num2==45:
    print(555)
elif operator=="+" and num1==56 or num1==9 and num2==9 or num2==56:
    print(77)
elif operator=="/" and num1==56 or num1==6 and num2==6 or num2==56:
    print(4)
else:
    if operator =="*":
        print(num1*num2)
    elif operator == "/":
        print(num1/num2)
    elif operator == "+":
        print(num1+num2)
    elif operator == "-":
        print(num1-num2)
    elif operator == "%":
        print(num1%num2)
    else:
        print("Invalid Operator")
