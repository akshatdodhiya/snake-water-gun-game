a, b = 9, 8  # New trick to initialize more than one variable
c = sum((a, b))  # Sum accepts only lists or tuple i.e it should be iterable for giving output
# In Pycharm - Press Ctrl + (click on the method) (here sum) to get the built in program of all the built in functions
# Functions also comes from modules
print(c)

# ----------------------------------------------User-Defined Functions--------------------------------------------------


def function1(p, q):  # 'def' is the keyword use to initialize a function # Function with parameters
    print("Hello you are in function-1", p + q)


function1(12, 6)


def function2(m, n):  # Function that do not return any value
    average = (m+n)/2
    print("Average is", average)  # Printing Average


function2(10, 12)


def func2(m, n):  # Function that returns any value
    """This function calculates the average of two numbers and return the final value"""
    # The above thing is called a Docstring , it is the first String in a class or method...
    # It is used to provide info about the function ...
    # It is always written in between Triple quotes
    avg1 = (m+n)/2
    return avg1  # Returning value of avg


avg = func2(4, 8)  # Storing the return value of func2 in variable avg
print("Avg is ", avg)  # Printing avg

print(func2.__doc__)  # This built in function (.__doc__) prints the Docstring of the user-defined function
