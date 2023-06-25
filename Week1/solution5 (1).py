str = input("Enter a string: ")
str = str.casefold() 
count = {x:sum([1 for char in str if char == x]) for x in 'aeiou'}
print(count)
