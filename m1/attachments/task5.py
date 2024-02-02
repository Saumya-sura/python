supermarket_bill = []

supermarket_bill.append('Milk')
print("After adding 'Milk':", supermarket_bill)

supermarket_bill.insert(1, 'Bread')
print("After inserting 'Bread' at position 1:", supermarket_bill)

supermarket_bill[0] = 'Juice'
print("After modifying first item to 'Juice':", supermarket_bill)

supermarket_bill.remove('Bread')
print("After removing 'Bread':", supermarket_bill)

supermarket_bill.clear()
print("After clearing the list:", supermarket_bill)

supermarket_bill = ['Juice', 'Milk', 'Eggs', 'Bread', 'Cheese']

sliced_items = supermarket_bill[1:4]
print("Sliced items:", sliced_items)

removed_item = supermarket_bill.pop(2)
print("Removed item at index 2:", removed_item)
print("List after removing:", supermarket_bill)

count_of_milk = supermarket_bill.count('Milk')
print("Number of times 'Milk' appears:", count_of_milk)

supermarket_bill.sort()
print("Sorted list:", supermarket_bill)

supermarket_bill.reverse()
print("Reversed list:", supermarket_bill)