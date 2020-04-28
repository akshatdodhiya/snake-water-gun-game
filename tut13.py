v = 4
v2 = 56

v3 = int(input())# storing input

if v3>v2:# using if else conditional statement
    print("Number is greater")
if v3==v2:
    print("Equal") #The TAB space after a colon in the condition or loop is known as indentation and error due to not leaving space is Indentation error
else:# colon represents entering into th condition of the statement
    print("Number is smaller")
#__________________________________PART-2_______________________________________________

print("Enter your age")
age = int(input())

if age>18:
    print("Yes, You are eligible for driving vehicle")
elif age==18:
    print("We cannot decide, you have to physically come for a test")
else:
    print("No, You are not eligible to drive vehicle")