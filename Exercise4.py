print("Enter the number of lines to print Stars")
n = int(input())  # Taking input as integer

print("Enter 1 - to print in ascending order\nEnter 0 - to print in descending order")
choice = bool(int(input()))  # Converting input in integer and then converting it to boolean

if choice:  # This if condition is the short-form of 'choice == True'
    for i in range(0, n):  # range() function generates numbers from 0 (by default) to the limit given after comma(',')
        for j in range(0, i+1):  # numbers are generated at each iteration
            print("*", end="")  # end statement helps to print asterisks in one single line

        print("\r")  # "\r" is escape sequence character which is used for carriage return, it simply returns the 

else:
    for i in range(n, 0, -1):
        for j in range(0, i):
            print("*", end="")

        print("\r")  # "\r" is escape sequence character which is used for carriage return
