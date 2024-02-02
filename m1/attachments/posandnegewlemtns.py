my_list = [2,-3,4,-5,6,-7,8,9,-10]
positive_count = 0
negative_count = 0

for i in my_list:
    if i >= 0:
        positive_count +=1
    else:
        negative_count +=1
        
print("Number of positive elements in the list are :", positive_count)
print("Number of negative elements in the list are :", negative_count)

