s = set() # empty set is declared
l = [1, 2, 3, 4] # list l is created

s_list = set(l) # list l is added to set s_list
#s_from_list = set([1, 2 ]) declaring a set without declaring a different list

print(s_list)
# print(s_from_list)
""" s_from_list is commented because of  some type in unexpected error though the program is running properly
but a highlight is made on values initialized to set s_from_list  """

s.add(1) # adding a value in a set
s.add(1)# though two times same nuber is added to the list but the number will be added only once
s.add(2)# adding different element in set 's'

s1 = s.union({1, 2, 3, 4}) # union of set s and 1,2,3,4 is made and stored in s1

print(s, s1)

s1.remove(3)# removing an element from set s1
print(s1)
s2 = s.intersection({1}) # intersection of set s and 1,2 is made and stored

print(s2, len(s)) # printing length of the set

print(max(s1), min(s))# printing minimum and maximum values in the sets

s3 = {6, 10, 8} # declaring set and initializing its values
print(s.isdisjoint(s3))# checking whether set s is disjoint with s3 or not