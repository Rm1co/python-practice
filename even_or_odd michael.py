def check_even_or_odd(num):
    # Check if the number is divisible by 2 (even)
    if num % 2 == 0:
        return "Even"  # Return "Even" if the number is divisible by 2
    else:
        return "Odd"  # Return "Odd" if the number is not divisible by 2
    
# Test case 1: Check if 22 is even or odd
test1 = 22
print(f"The number {test1} is {check_even_or_odd(test1)}")

# Test case 2: Check if 19 is even or odd
test2 = 19
print(f"The number {test2} is {check_even_or_odd(test2)}")
