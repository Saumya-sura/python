
from collections import Counter
#Counter class is a special type of object data-set provided with the collections module in Python3. Collections module provides the user with specialized container datatypes, thus, providing an alternative to Python’s general-purpose built-ins like dictionaries, lists, and tuples. 

#Counter is a sub-class that is used to count hashable objects. It implicitly creates a hash table of an iterable when invoked.

color1 = ["red", "orange", "green", "blue", "white"]
color2 = ["black", "yellow", "green", "blue"]

counter1 = Counter(color1)
counter2 = Counter(color2)

print("Color1-Color2: ", list(counter1 - counter2))

print("Color2-Color1: ", list(counter2 - counter1))

