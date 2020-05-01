import time

k = 0
initial = time.time()  # This function returns exact time and it's ticks (name given to its return value)
# are getting incremented in each second

while k < 50:  # Running while loop 50 times
    print("Hello World! How are you")
    k += 1  # Incrementing value of k
print(f"While loop took: {time.time() - initial} Seconds")  # Printing the time taken by while loop to execute
# 'time.time() - initial' subtracts the time before execution of above code from the time after executing the above code

initial2 = time.time()  # Taking and storing time before executing for loop
for i in range(50):  # Executing for loop for 50 times
    print("Hello World! How are you")
print(f"For loop took: {time.time() - initial2} Seconds")

print("\n\n")

# --> Printing local time of an area

localtime = time.asctime(time.localtime(time.time()))
print(localtime)
"""
LOGIC : time.time() - It returns exact time calculated by counting from old time or from somewhere
        time.localtime() - It converts the time returned by above function in local time
        time.asctime() - The time converted by localtime is in tuple so It converts it into readable format
"""

for i in range(5):
    print("This are ending lines")
    time.sleep(1)  # This function makes the program to stop executing for the seconds provided in parenthesis
