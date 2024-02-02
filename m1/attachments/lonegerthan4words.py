n=4
str="Find the List of Words that are Longer than n from a given List of Words"
new_list = []
text = str.split(" ")
for x in text:
	if len(x) > n:
		new_list.append(x)
print(new_list)