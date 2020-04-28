f = open("akshat2.txt", "w")  # "w" opens the file in write mode, # If the name of the file entered is not present
# already then it will create the file
f.write("Akshat is beginner in programming but doing well")  # This function removes the before present content of the
# file and adds the string in that file.

no_of_characters = f.write(" Hello World")  # Storing the number of characters written by 'f.write()' function
print(no_of_characters)
g = open("akshat3.txt", "a")  # "a" opens the file in append mode in which the string or anything will be added as many
# times the program is being run
g.write("\n!!Never loose hope!!\n")

h = open("akshat4.txt", "r+")  # others files are already opened in different modes hence new file is created

# Note - First read() function should be used and then write function should be used to run the program properly
# "r+" mode opens the file in read and append at same time if the above note is followed

print(h.read())
h.write("\nHow are you all ?")
h.write("\nHello World :)")


# Note - If file is once opened in write or read or in any other mode then the same file cannot be again used in any
# other mode hence above I've created two files "akshat2.txt" and "akshat3.txt"

f.close()  # Closing is necessary after opening the file
g.close()
h.close()
