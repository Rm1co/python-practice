def reverse_string(s):
    # Initialize an empty string to hold the reversed string
    reversed_str = ''
    
    # Loop through each character in the original string
    for char in s:
        # Prepend the current character to the reversed string
        reversed_str = char + reversed_str
    
    # Return the reversed string after the loop finishes
    return reversed_str
    
# Test case 1: Reverse the string "hello"
test1 = "hello"
print(f"Reversed string is {reverse_string(test1)}")

# Test case 2: Reverse the string "Michael"
test2 = "Michael"
print(f"Reversed string is {reverse_string(test2)}")
