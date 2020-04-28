i = 0 #Initializing a value to variable i

while (True): #Using while loop with condition i<45

    if (i+1<5):
        i = i + 1  #Increment should be done in each condition so as to run program perfectly
        continue #By this keyword control(program) will jump to next iteration till the value of i is less than 5

    if (i==44):

        i = i + 1  # Incrementing the value of i by 1 in each iterartion
        break #By this keyword loop will stop iterating and will terminate

    print(i + 1, end=" ")  # Printing different values of i
    i = i + 1  # Incrementing the value of i by 1 in each iterartion


#________________________________[ QUIZ ]__________________________________________

while (1): # 1 in condition is same as True
    n = int(input("Enter your number\n"))

    if (n>=100):
        print("Congratulations!! You have entered a number greater than or equal to 100 so loop is terminating\n")
        break
    else:
        print("Try Again!!\n")
        continue


