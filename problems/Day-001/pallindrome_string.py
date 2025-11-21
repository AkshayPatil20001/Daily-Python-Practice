
# Detail,Description
# Problem Statement,"Write a function that takes a string as input, 
# returns the reversed version of the string, and also checks if the original string is 
# a palindrome (reads the same forwards and backward, ignoring case)."
# Input,"A string, e.g., ""madam"""
# Output,"A tuple: (reversed_string, is_palindrome_boolean)"
# Example 1,"Input: ""Level"" → Output: ('level', True)"
# Example 2,"Input: ""Python"" → Output: ('nohtyp', False)"

def reverse_and_check_palindrome(input_string):
    # Reverse the string
    reversed_string = input_string[::-1]
    
    # Check if the original string is a palindrome (case insensitive)
    is_palindrome = input_string.lower() == reversed_string.lower()
    
    return (reversed_string, is_palindrome)

# Example usage
print(reverse_and_check_palindrome("Level"))  # Output: ('leveL', True)