# Problem Statement	Write a function that takes a string as input, 
# returns the reversed version of the string, and also checks if the original 
# string is a palindrome (reads the same forwards and backward, ignoring case).


def rev_str(str1):

    if str1==str1[::-1]:
        print("Pallindrome")
    else:
        print("Not Pallindrome")
str1=input(" :").lower()
rev_str('')