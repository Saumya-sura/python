#Write a Python program to insert a given string at the beginning of all items in a list.
my_list = ['apple', 'banana', 'orange']
prefix = 'fruit - '
result = [prefix + item for item in my_list]

print(result)