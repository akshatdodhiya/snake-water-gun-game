def getdate():
    import datetime
    return datetime.datetime.now()


choice = bool(int(input("Enter 0 for retrieving data and 1 for locking data\n")))

if choice:
    name = input("\nEnter the name of which you want to lock data\n")
    name.lower()
    Choice = bool(int(input("\nEnter 0 for Exercise and 1 for Food\n")))
    if Choice:
        food = input("Enter the name of the food that you took\n")
        # Syntax for naming variable = name of person , food/exercise, Mode in which file is opened
        if name == "akshat":
            with open("akshat_food.txt", "a") as afa:  # afa = Akshat Food in Append
                afa.write(str(getdate().strftime("%Y-%m-%d %H:%M:%S")))
                afa.write("\t")
                afa.write(food)
                afa.write("\n")

        elif name == "sujal":
            with open("sujal_food.txt", "a") as sfa:  # sfa = Sujal Food in Append
                sfa.write(str(getdate().strftime("%Y-%m-%d %H:%M:%S")))
                sfa.write("\t")
                sfa.write(food)
                sfa.write("\n")

        elif name == "akbar":
            with open("akbar_food.txt", "a") as dfa:  # dfa = Dad Food in append
                dfa.write(str(getdate().strftime("%Y-%m-%d %H:%M:%S")))
                dfa.write("\t")
                dfa.write(food)
                dfa.write("\n")

        else:
            print("Invalid name please enter a valid one")

    else:
        Exercise = input("\nEnter the name of the Exercise you did\n")
        if name == "akshat":
            with open("akshat_Exercise.txt", "a") as aea:  # aea = Akshat Exercise in Append
                aea.write(str(getdate().strftime("%Y-%m-%d %H:%M:%S")))
                aea.write("\t")
                aea.write(Exercise)
                aea.write("\n")

        elif name == "sujal":
            with open("sujal_Exercise.txt", "a") as sea:  # sea = Sujal Exercise in Append
                sea.write(str(getdate().strftime("%Y-%m-%d %H:%M:%S")))
                sea.write("\t")
                sea.write(Exercise)
                sea.write("\n")

        elif name == "akbar":
            with open("akbar_Exercise.txt", "a") as dea:  # dea = Dad Exercise in Append
                dea.write(str(getdate().strftime("%Y-%m-%d %H:%M:%S")))
                dea.write("\t")
                dea.write(Exercise)
                dea.write("\n")

        else:
            print("Invalid name please enter a valid one")

else:
    name = input("\nEnter the name of which you want to retrieve data\n")
    name.lower()

    r_choice = bool(int(input("\nEnter 1 for retrieving Exercise data and 0 for Food data\n")))
    if r_choice:
        if name == "akshat":
            with open("akshat_Exercise.txt") as aer:  # aer = Akshat Exercise in Read
                print(aer.read())

        elif name == "sujal":
            with open("sujal_Exercise.txt") as ser:  # ser = Sujal Exercise in read
                print(ser.read())

        elif name == "akbar":
            with open("akbar_Exercise.txt") as der:  # der = Dad Exercise in read
                print(der.read())

        else:
            print("Invalid name please enter a valid one")
    else:
        if name == "akshat":
            with open("akshat_food.txt") as afr:  # afr = Akshat food in read
                print(afr.read())

        elif name == "sujal":
            with open("sujal_food.txt") as sfr:  # sfr = Sujal food in read
                print(sfr.read())

        elif name == "akbar":
            with open("akbar_food.txt") as dfr:  # dfr = Dad food in read
                print(dfr.read())

        else:
            print("Invalid name please enter a valid one")
