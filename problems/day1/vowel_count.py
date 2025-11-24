# Write a function that takes a string and counts the total occurrences of 
# vowels (a, e, i, o, u), case-insensitive, returning a single integer count.


str1='akghteqop'
vowels='aeiou'
count=0
for i in str1.lower():
    if i in vowels:
        count=count+1
print(count)