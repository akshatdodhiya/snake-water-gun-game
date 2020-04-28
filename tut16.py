list1 = ["Akshat", "Krish", "Tanush", "Akshat Shah", "Rishabh"]#List can be iterated

for items in list1:#items is the name of a variable
    print(items)

tuple1 = ("Akshat", "Krish", "Tanush", "Akshat Shah", "Rishabh")#Tuples can be iterated but not all datatypes can be iterated

for item in tuple1:#For loop used to print items in tuple and lists
    print(item)#Tuple is printed

list2 = [["Akshat", "Football"], ["Krish", "Basketball"], ["Tanush", "Handball"],
         ["Akshat Shah", "Cricket"], ["Rishabh", "Cricket"]]#Numbers can also input instead of strings

for item in list2:
    print(item)#Prints lists in list

for name , sport in list2:
    print(name, "Plays", sport)#Prints individuals items in lists in list

dict1 = dict(list2)#Casting list to dictionary

print(dict1)#Printing the dictionary dict1

# for name, sport in dict1:  # dictionary cannot be iterated and printed directly as lists and tuple
#     print(name ,"Plays", dict1)
#The above two line code shows error and correction of that error is below

for name, sport in dict1.items(): #.items() function is used to iterate items in the dictionary
    print(name, "does not plays", sport)

#To print only keys of a dictionary it can be done simply through lists method

for key in dict1:#Keys are the main things in dictionary e.g "Akshat", "Rishabh", etc. are keys of dict1
    print(key)

#--------------------------------PART-2-------------------------------------------------------

#Use of if-else in for loop
for name, sport in dict1.items():#Variable name in the for-loop cannot be same as any list or tuple or etc.
    if name=="Akshat" or name=="Akshat Shah" or name=="Tanush":
        print(name, "Likes", sport)
    elif name=="Krish":
        print(name, "Plays", sport)
    else:
        print(name, "Doesn't Likes", sport)
#----------------------------PART-3-----------[QUIZ]-----------------------------------------

#Program to print all the numbers greater than or equal to 6

list3 = ['a', 2, 'b', 9, 'c', 7, 'd', 8]

for number in list3:
    if str(number).isnumeric() and number>=6:#isnumeric() function is used to check
        print(number)
