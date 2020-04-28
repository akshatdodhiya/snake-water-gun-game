a = input("Enter num1\n")
b = input("Enter num2\n")

"""
Try and except Exception Handling - is same as try and catch in java...
It is used to catch the error and print the error and prevent the program from breaking at the error point
This function is used to execute codes written after the error line...
It is mainly used in Programs that are related to Internet
"""

try:  # Any Statement in this can run as trial and if it shows any error then the error will go in except block
    print("The sum of these two numbers is",
          int(a) + int(b))

except Exception as e:  # 'e' is the name of the variable in which the message of error is stored # 'as' is a keyword
    print(e)  # Printing the error as a String message

print("\nThis is the example of Important lines after the error line")
