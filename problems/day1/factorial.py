# Write a function that accepts a positive integer $n$ and calculates 
# its factorial ($n!$), which is the product of all positive integers less than or 
# equal to $n$. You can solve this iteratively or recursively.

def factorial(num):
    fact=1
    if num==1 or num==0:
        return 1
    else:
        while num >1:
            fact=fact*num
            num=num-1

    return fact
print("Factorial is :",factorial(4) )