f = open("akshat.txt")

print(f.tell())  # This function tells about the position of the file reading pointer
print(f.readline())  # This function reads & prints one line from file
print(f.tell())
print(f.readline())  # Running this function again will read & print next line from the file
print(f.tell())

f.seek(0)  # This function shifts the reading pointer of a file to the position provided in parenthesis
# It is not necessary that the number in seek() function should be zero it can be any number
# but number greater than the actual total characters in file will return empty
# The above function is used when you have to print the same statement more than once from the same file
print(f.readline())  # Now it will print the first line from the file

# Note - if seek() function is used before tell() function then the tell() function will show the number
# which is provided in seek() function as seek() function moves the reading cursor to the number in parenthesis

f.close()
# -----------------------------------------------TUT-31---------------------------------------------------------------

# Opening and closing a file using with bloc
with open("akshat.txt") as g:  # This method is same as opening and closing a file through above simple techniques
    a = g.readlines()  # Reading a line in file and storing in a
    print(a)  # printing the first line of file stored in a
