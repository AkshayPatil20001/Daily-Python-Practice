# Given a list of $n-1$ distinct integers in the range of 1 to $n$, 
# find the one missing integer. Assume the list is unsorted and contains no duplicates.

list1=[8, 6, 7, 5, 3, 0, 9, 1, 2]
n=10
lst=[]
unique=[]
for i in range(n):
    lst.append(i)
#print(lst)
flag=0
for i in lst:
    if i not in list1:
        unique.append(i)
print("Missing element is",int(unique[0]))


# Another approach
lst=[0,1,3,4,6,7,2,]
n=len(lst)
sum_actual=sum(lst)
sum_original=((n+1)*n)/2
print("Missing element is",(sum_original-sum_actual))