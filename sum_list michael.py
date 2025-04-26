def sum_list(numbers):
    # Initialize sum to 0, which will hold the sum of the list elements
    sum = 0
    
    # Loop through each number in the list and add it to the sum
    for num in numbers:
        sum += num
    
    # Return the total sum of the list elements
    return sum
    
# Test case 1: Sum the numbers in the list [7, 8, 9, 10]
test1 = [7, 8, 9, 10]
print("sum: ", sum_list(test1))

# Test case 2: Sum the numbers in the list [50, 60, 70]
test2 = [50, 60, 70]
print("sum: ", sum_list(test2))

# Test case 3: Sum the numbers in the list [-5, 15, 25]
test3 = [-5, 15, 25]
print("sum: ", sum_list(test3))
