l = 10  # Global Variable
k = 10


def function1(n):
    l = 5  # Local variables
    # Though the value of l is 10 in global but in function first preference is given to local variables
    # If 'l' is not initialized in function then it's value will come from global scope i.e. global variable's value
    m = 8
    print(l, m)
    print(n, "I have printed")

    global k  # 'global' keyword allows the function to edit/change the value of global variable
    # Without the global keyword, the function cannot change the value of global variable
    k = k + 45
    print(k)


# Local variables cannot be used as global, meaning that it cannot be used outside the function
# Example - here print(m) will give error as ~ NameError: name 'm' is not defined because 'm' is a local variable

function1("Hello")
print(l)


# Press "Ctrl + D" for duplicating a line

# ------------------------------------------------    PART - 2    -----------------------------------------------------


def akshat():
    x = 20  # This is not a global variable

    def sujal():  # This types of methods are called nested methods
        global x  # It will check x outside of all methods
        x = 88  # After not getting variable 'x' it will be initialized as 88

    print("x's value before calling sujal()", x)
    sujal()  # Calling function sujal()
    print("x's value after calling sujal()", x)


# In the above method x's value is not changed because "global x" will look for variable 'x' globally instead of it's
# parent function
akshat()  # Calling function akshat()

print(x)  # Here the value of 'x' will be 88 as in def sujal() variable x is checked globally but after not getting any
# variable 'x' declared globally it had created a variable named 'x' with value 88
