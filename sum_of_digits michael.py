def sum_of_digits(n):
    # Initialize total to 0, which will hold the sum of digits
    total = 0
    
    # Loop through each digit of the number until n becomes 0
    while n > 0:
        # Add the last digit of n to the total (n % 10 gives the last digit)
        total += n % 10
        
        # Remove the last digit from n (n // 10 drops the last digit)
        n = n // 10
    
    # Return the total sum of digits
    return total

# Test case 1: Find the sum of digits of 789
test1 = 789
print(f"Sum of digits of {test1} is {sum_of_digits(test1)}")

# Test case 2: Find the sum of digits of 512
test2 = 512
print(f"Sum of digits of {test2} is {sum_of_digits(test2)}")
