mystr = "Hello Akshat How Are You"
print(mystr)
print(len(mystr))
print(mystr[6:12])
# Note :  ":" represents slicing of string and left end (Index Numbers) represents beginning of string
# Right end represents finishing of the string. But the number on right end gives result 1
# less than what is written.

print(mystr[0:12:2]) #Advanced Slicing

# Note : number after second colon(:) represents no. of letters to be skip while printing string this
# also to one while skipping the letters.

print(mystr[-4:-1])
# negative numbers represents counting of string from right side

print(mystr[::-1])
# negative number in skipping represents reversing of the string and then skipping as per no. give there

print(mystr.isalnum())
#checking is mystr alpha numeric

print(mystr.endswith('u'))
# string can also be checked with ends with

print(mystr.replace("Hello","Hi!"))
# Replaces the word on left of comma to right of comma
# Note : Letters (alphabets) can be used in place of words/strings

print(mystr.count(chr(117)))
# 117 is ASCII value for 'u'

print(mystr.count('w'))
#counting no. of w's in string

print(mystr.find("Akshat"))
# Basically used in big strings to find letter/word

print(mystr.capitalize())
# Capitalizes the first letter of the string

print(mystr.lower())
# Converts the string in lower case

print(mystr.upper())
# Converts the string in Upper Case