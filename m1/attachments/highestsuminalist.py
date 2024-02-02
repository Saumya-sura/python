my_list = [[1, 2, 3], [4, 5, 6], [10, 11, 12], [7, 8, 9]]
max_sum = 0
result = []
for sub_list in my_list:
    current_sum = sum(sub_list)
    if current_sum > max_sum:
        max_sum = current_sum
        result = sub_list
print("The list in my_list with the highest sum is:", result)
