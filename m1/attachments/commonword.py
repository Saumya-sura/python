string1 = input("Enter the first string: ")
string2 = input("Enter the second string: ")


string1 = string1.lower()
string2 = string2.lower()

# split the strings into words
words1 = string1.split()
words2 = string2.split()


common_words = []
for word in words1:
    if word in words2 and word not in common_words:
        common_words.append(word)

if len(common_words) > 0:
    print("The common words are:", ', '.join(common_words))
else:
    print("There are no common words.")

