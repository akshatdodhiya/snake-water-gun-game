# Factorial calculation equation - n * (n-1) * (n-2) * (n-3) ..... 1 * n


def factorial_iterative(n):  # Iterative means using iteration i.e loops  # It is called Iterative Approach
    """
    :param n: Integer
    :return: n * (n-1) * (n-2) * (n-3) ..... 1
    """
    fac = 1
    for i in range(n):
        fac = fac * (i+1)
    return fac


def factorial_recursive(n):  # Recursive means repeating method n number of times by calling method inside a method
    # It is called Recursive Approach
    """
    :param n: Integer
    :return: n * (n-1) * (n-2) * (n-3) ..... 1
    """
    if n == 1 or n == 0:  # 0! or 1! is 1 by definition
        return 1
    else:
        return n * factorial_recursive(n-1)


"""
Logic - if inp = 5

5 * factorial_recursive(4)
5 * 4 * factorial_recursive(3)
5 * 4 * 3 * factorial_recursive(2)
5 * 4 * 3 * 2 * factorial_recursive(1)  # Now in this case recursion will stop and function will return 1
5 * 4 * 3 * 2 * 1 = 120 is the final value will be returned

"""
number = int(input("Enter the number\n"))
print("Factorial using iterative method is", factorial_iterative(number))
print("Factorial using recursive method is", factorial_recursive(number))

# -------------------------------------------------------  QUIZ  ----------------------------------------------------


def fibonacci(n):  # Using Iteration
    last = 0
    previous = 1

    if n == 1:
        print("Fibonacci series =", last)
    elif n == 2:
        print("Fibonacci series =", last, previous)
    else:
        print("Fibonacci series = 0  1", end="  ")

        for i in range(n-2):  # (n-2) because first two terms are already printed
            current = last + previous
            last = previous
            previous = current
            print(current, end="  ")


def fibonacci_recursive(n):
    if n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        return fibonacci_recursive(n - 1) + fibonacci_recursive(n - 2)


num = int(input("Enter the total number of digits you want to print\n"))
fibonacci(num)
print("\nFibonacci's position using recursion", fibonacci_recursive(num))
