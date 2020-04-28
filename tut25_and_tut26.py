"""
File IO Basics
"r" (Read Mode) - Opens file for reading (This is default mode)
"w" (Write mode) - Opens file for Writing
"r+" (Read Plus Mode) - Opens file for reading and writing both
"x" (Exclusive creation) - Creates file if it does not exists and it won't work if the file already exists
"a" (Append) - Adds more content to a file
"t" (Text mode) - File contains text i.e txt file [This function is used when you have to deal with strings]
"b" (binary mode) - Deals with binary files
"+" (plus mode) - Used to update files i.e to read & write
"""
# -------------------------------------------TUT - 26------------------------------------------------------------------

f = open("akshat.txt", "rt")  # This functions opens the file in variable 'f'
# "r" is read mode and "rt" means read mode in txt format.
g = open("akshat.txt", "rb")
# "rb" is read mode in Binary format
h = open("akshat.txt", "rt")

content = f.read()  # Through this method you can read the contents of file and store in a variable
# Note : It is function not mode
print(content)  # Printing the contents of the file

content1 = h.read(3)  # It will print first three characters from the file
print(content1)

content1 = h.read(3)  # It will print next three characters from the file
print(content1)

content1 = h.read(3455656)  # It will ony print maximum number of characters present in it if the number more
# than its actual length is given
# If the above type of function is run again then it will print empty i.e nothing
print("1", content1)

content1 = h.read(3455656)
print("2", content1)  # Nothing will be printed after "2"

print(g.read())  # Printing contents of file in binary format, in output it is in single inverted commas
# with b in beginning

i = open("akshat.txt")
# content  = i.read()  # This line is commented because while printing line by line it gives empty output
# as file is already read by this statement

#  Note : If the file is read once then the file pointer will be empty and hence nothing can be get when iterated

for line in i:  # It reads the file line by line
    # If 'i' is replaced with content then it will read character by character
    print(line, end="")  # 'end=""' proves that though ending is empty it is by default that new line is being printed

print("\n")

j = open("akshat.txt")
print(j.readline())  # This function helps to read the line of the file
print(j.readline())  # Using this function again prints the next line
print(j.readline())

k = open("akshat.txt")
print(k.readlines())  # This function prints all its lines in one list with different elements of different lines

f.close()  # This 'close' function is necessary every time when you open a file
g.close()
h.close()
i.close()
j.close()
k.close()
