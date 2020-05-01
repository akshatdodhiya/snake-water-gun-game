# ------------------------------------------------ Old (Simple)Method to take parameters ------------------------------
def function_to_name_printing(a, b, c):  # Taking parameters to print names of the users
    print(a, b, c)  # Printing the names of the user


function_to_name_printing("Akshat", "Raj", "Alex")  # Calling the functions and giving the names

print("_______________________________")


# --> The Above method is not efficient if the parameters/names of the user increases as it takes only limited arguments

# ------------------------------------------------ New(Complex) Method to take parameters ------------------------------

# --> Note : The system of writing the parameters in a function is first - normal parameters, second - *args,
# third - *kwargs.

def name_printing(introduction, *args, **kwargs):
    # --> Asterisk before args is necessary so as to get parameters in tuple without any errors

    # --> args and kwargs can be replaced with any other name but asterisks are necessary

    print(args[0])  # Printing the value at Index number zero
    print(type(args))  # 'tuple' because it is known as convention. It is default.

    # Though list or tuple or anything is passed to args but the final type from which it will take will be tuple only.

    print(introduction)  # Normal parameter can be added with *args

    for items in args:  # --> Through this method 'n' numbers of items can be printed and if anything is added to the
        # list then it can handle that too
        print(items)  # Printing each items in tuple args

    for key, value in kwargs.items():  # Using for loop to take keys and values of dictionary kwargs
        print(f"{key} Plays {value}")  # Printing f String


names = ["Akshat", "Raj", "Alex", "Steven", "Tony"]  # Initializing a list
intro = "Students are :"  # Simple variable
kw = {"Akshat": "Football", "Harsh": "Cricket", "James": "Handball", "Steve": "Volleyball"}  # Initializing dictionary

name_printing(intro, *names, **kw)  # Asterisk is necessary to pack the list or tuple to send as a parameter in function
