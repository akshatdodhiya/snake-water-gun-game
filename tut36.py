# Lambda functions or Anonymous functions
# --> Lambda is a function which is not a function means it works same as a function but it is not an actual function
# --> Lambda is not necessary but due to many programmers use it one should know the concept of lambda
# --> Lambda is the new way of creating function


def minus(a, b):  # This is a function which return the subtracted value
    return a - b


subtract = lambda x, y: x - y  # This works same as "def minus(a, b)"
# If the above 'lambda' is converted to function by suggestions given on that line then it will look same as
# "def minus(a, b)"

print("Function : ", minus(9, 4), "Lambda :", subtract(9, 4))

# ------------------------------------------------- using lambda for sorting ------------------------------------------


# def a_first(a):  # This is an example of sorting using function
#     return a[1]
a = [[4, 7], [7, 4], [9, 5]]
# a.sort(key=a_first)  # This is the part of sorting using function

a.sort(key=lambda x: x[1])
# --> The above statement means that lambda will create a function which will return the value on index number 1 of
# any input given to it
# --> It is the property of sort function that it takes 'key=' as a function's name as written on line 23
print(a)
