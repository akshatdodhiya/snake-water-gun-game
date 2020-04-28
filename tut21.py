# ______________________Arithmetic Operators______________________________________________
print("\nArithmetic Operators\n")
print("5 + 6 is", 5 + 6)
print("5 - 6 is", 5 - 6)
print("5 * 6 is", 5 * 6)
print("5 / 6 is", 5 / 6)
print("5 % 6 is", 5 % 6)
print("15 // 6 is", 15 // 6)  # // gives an Integer value of division
print("2 ** 3 is", 2 ** 3)  # ** is exponential function

# _______________________Assignment Operators____________________________________________
print("\nAssignment Operators\n")
x = 25
print(x)
x = x % 7  # /= , += , -= , %=(percent equals to) , are its different types
print(x)

# _______________________Comparison Operators____________________________________________
print("\nComparison Operator\n")
i = 6
print(i == 6)  # != , > , >= , < , <= are its different types

# _______________________Logical Operators____________________________________________
print("\nLogical Operators\n")
a = True
b = False
print(a and b)  # It works on principle of boolean algebra
# this principle is same as like signs gives + and unlike signs gives -
# In 'and' operator if both true then only it will return true
print(a or b)
# In 'or' operator if any one is true then it will return true
# _______________________Identity Operators____________________________________________
print("\nIdentity Operators\n")
print(a is b)  # it is same as a == b
print(a is not b)  # it is same as a != b
# numbers can also be operated through 'is' and 'is not' operator
# _______________________Membership Operators____________________________________________
print("\nMembership Operators\n")
list1 = [3, 3, 4, 39, 45, 9]
print(4 in list1)
print(9 not in list1)  # Returns True or False
# _______________________Bitwise Operators____________________________________________
# Operators that works with Bit or binary numbers (0, 1) are known as Bitwise Operators
print("\nBitwise Operators\n")
# Examples of Binary numbers
# 0 = 00
# 1 = 01
# 2 = 10
# 3 = 11
print(0 | 1)  # '|' is 'or' operator and checks each unit of both the arguments.
# E.g - ten's place (0 or 0 = 0) one's place(0 or 1 = 1) therefore 01 = 1 (given above) hence answer is one
print(0 & 1)  # '&' is 'and' operator
print(0 | 3)  # Ten's place (0 | 1 = 1) , unit's place (0 | 1 = 1) return of argument = 11 = 3 (above given : binary for 3)
