def calculate_stats(lst):
   
    total = 0
    minimum = float('inf')
    maximum = float('-inf')
    count = len(lst)

    for value in lst:
        total += value
        if value < minimum:
            minimum = value
        if value > maximum:
            maximum = value


    return total, minimum, maximum, count


values = [1, 2, 3, 4, 5]
total, minimum, maximum, count = calculate_stats(values)
print("Total: ", total)
print("Minimum: ", minimum)
print("Maximum: ", maximum)
print("Count: ", count)

