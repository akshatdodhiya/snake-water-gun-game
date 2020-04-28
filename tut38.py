import random  # Press 'Ctrl + left click' on name of the module to open its backend code
# --> Type name of the module on google to get it's documentation for getting the names of its function as
# it's not necessary to remember the names of sub-modules or functions of a module
# Note : Always compare the version of python you are using with the version of python module documentation you searched

random_number = random.randint(0, 5)  # This statement gives the random number between 0 to 5 including 0 and 5
print(random_number)

random_num = random.random()  # random is name of the module and .random means that random function in that module
# --> It will generate numbers (not integers) between 0 to 1
# --> To print numbers between 0 to 100 just multiply line no. 9 with 100
print(random_num)
print(random.random.__doc__)  # Printing Docstring of function random in random module

# --> Printing Random choice

lst = ["DD1", "Zee TV", "Cartoon Network", "Star Plus"]  # Initializing a list 'lst'
choice = random.choice(lst)  # Using choice() function to choose any element of the list 'lst' randomly

print(choice)  # Printing the random choice
