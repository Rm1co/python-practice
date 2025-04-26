def factorial_loop(n):
    # Initialize result variable to 1 (since the factorial of 0 is 1)
    result = 1
    
    # Loop through numbers from 1 to n (inclusive)
    for i in range(1, n + 1):
        # Multiply result by current number i
        result *= i
    
    # Return the calculated factorial
    return result

# Test case 1: Find the factorial of 5
test1 = 5
print(f"Factorial of the number {test1} is {factorial_loop(test1)} ")

# Test case 2: Find the factorial of 4
test2 = 4
print(f"Factorial of the number {test2} is {factorial_loop(test2)} ")
