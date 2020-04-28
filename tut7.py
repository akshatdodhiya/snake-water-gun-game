var1 = "Hello World "
# Note :  var1 is name of a string variable by default
var2 = 5 # Integer point literal
var3 = 8.2
# Note :  here decimals are stored in floating point literal by default
var4 = "Akshat \n"

var5 = "44"

var6 = "56.7"

print(var1)
print(var2+var3)
print(var1+var4)
print(int (var5) + float (var6))
# Note : Strings and integer/float cannot be added or mathematically treated
print(3 * var4)
# Number multiplied by only any string prints the same string same number of time of which it is multiplied
print(100 * str(int (var5) + float (var6)))

#------------------------------------------------------PART~2---------------------------------------------------------

print("Enter your number")
inp = input()
# Inputs are generally stored in string format
print("You entered", inp)
print("Your Added Number is", int(inp)+10)
# int() changes the format of inp from string to integer