# Write a function that takes a list of integers and 
# returns the sum of all elements in the list.

def sumlist(mylist):
  sum=0
  for i in mylist:
    sum=sum+i
  return sum
print("Sum is ",sumlist([23,43,56,7]))