# create a tuple
student_info = ("John", "Doe", 20, "Male")

# a. print an item of the tuple
print(student_info[1])  # output: Doe

# b. check if an element exists within a tuple
if "John" in student_info:
    print("John exists in the tuple")

# c. check number of times an item has repeated
print(student_info.count("John"))  # output: 1

# d. remove an item from a tuple
# note: tuples are immutable, but we can convert it to a list first, then convert it back to a tuple after removing an item
list_info = list(student_info)
list_info.remove(20)
student_info = tuple(list_info)
print(student_info)  # output: ('John', 'Doe', 'Male')

# e. Slice a tuple
print(student_info[0:2])  # output: ('John', 'Doe')

# f. get the index of an item of the tuple
print(student_info.index("Doe"))  # output: 1

# g. print the size of a tuple
print(len(student_info))  # output: 3

# h. modify items of a tuple
# note: tuples are immutable, so we have to convert it to a list first
list_info = list(student_info)
list_info[2] = 21
student_info = tuple(list_info)
print(student_info)  # output: ('John', 'Doe', 21, 'Male')

