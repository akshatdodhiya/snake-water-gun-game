d = {"Akshat":"football","Harsh":"Cricket","Nayan":"Basketball","akshat":{"Game":"football","hobby":"computers"}}
d["sujal"] = "Hockey"
d[442] = "Nothing" #updating or adding to a dictionary
d[420] = "Lazy" #updating or adding to a dictionary
d.update({"Krish":"kabaddi"}) #updating or adding to a dictionary

print(d["akshat"]["Game"])
print(d)
del d[420] #Delete Function used to delete something from the dictionary

print(d) #Printing the whole dictionary
print(d.keys()) #Printing keys included in dictionary
print(d.items()) #Printing the items included in the dictionary

d3 = d
del d3[442] #Deleting from d3
print(d) #Got deleted from d

d2 = d.copy() #Making copy of d and storing in d2
del d2["akshat"] #Deleting from d2
print(d2) #Got deleted from d2
