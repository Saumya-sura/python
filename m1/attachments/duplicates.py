my_list = [1, 2, 3, 4, 2, 1, 5]

new_list = []

for i in my_list:
  if i not in new_list:
    new_list.append(i)

print(new_list)

