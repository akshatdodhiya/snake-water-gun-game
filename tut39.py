import math
# F Strings
# --> Method one for formatting the String

me = "Akshat"
a = "This is %s" % me  # This line adds String 'me' in the end of String a
print(a)

# --> Method two for formatting the String

me1 = "akshat"
z = 5
b = "This is %s %s" % (me1, z)  # This line formats file and adds two strings (formed tuple) in 'b'
# %d requires a number , %s requires a string , %c requires char value
print(b)

# --> Method three for formatting the String

me3 = "akshat"
x = 9
c = "I am {} {}"  # {} represents elements to be entered in this String
d = "Hello {1} {0}"  # Numbers inside {} represents the index numbers of the tuple's elements
op = c.format(me3, x)  # This function formats the String
op2 = d.format(me3, x)  # Formatting the String by entering the tuple in the String
print(op)  # Printing the output
print(op2)  # Printing the output

# --> Method four for formatting the String

e = f"hi Everyone {me} {z} {math.cos(65)}"
# --> Any String beginning with 'f' is know as F String, Full form of F String - Fast String :)
# --> You can directly add elements in the curly brackets, This method is modified version of method three
# --> Any function or module can also be used inside the curly brackets
print(e)
