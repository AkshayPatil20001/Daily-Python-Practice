"""
Problem Statement:
Write a function that takes a string as input, returns the reversed version 
of the string, and also checks if the original string is a palindrome.
"""

def analyze_string(text):
    # 1. Convert to lowercase so 'Level' matches 'level'
    clean_text = text.lower()
    
    # 2. Reverse the string using slicing [start:stop:step]
    # A step of -1 reverses the string.
    reversed_text = clean_text[::-1]
    
    # 3. Check if the original equals the reverse
    is_palindrome = (clean_text == reversed_text)
    
    # 4. Return the tuple
    return reversed_text, is_palindrome

# --- Testing the Examples ---

# Example 1
result1 = analyze_string("Level")
print(f"Input: 'Level' -> Output: {result1}") 
# Expected: ('level', True)

# Example 2
result2 = analyze_string("Python")
print(f"Input: 'Python' -> Output: {result2}") 
# Expected: ('nohtyp', False)