def factorial_recursive(n):
    # Base case: if n is 0 or 1, return 1 as the factorial of 0 and 1 is 1
    if n == 0 or n == 1:
        return 1
    else:
        # Recursive case: multiply n by the factorial of n-1
        return n * factorial_recursive(n - 1)
    
# Test case 1: Find the factorial of 6
test1 = 6
print(f"Factorial of the number {test1} is {factorial_recursive(test1)} ")

# Test case 2: Find the factorial of 2
test2 = 2
print(f"Factorial of the number {test2} is {factorial_recursive(test2)} ")
