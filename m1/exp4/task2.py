veg_menu = ["Veg Roll", "Noodles", "Fried Rice", "Manchurian", "Soup"]
non_veg_menu = ["Chicken Roll", "Noodles", "Fried Rice", "Chilli Chicken", "Soup"]

def order(preference, order_list):
    menu = []
    if preference == "veg":
        menu = veg_menu
    elif preference == "non-veg":
        menu = non_veg_menu
    else:
        print("Enter a valid preference")
        return
    for index, item in enumerate(menu):
        print(index+1, item)
    choice = int(input("Enter your choice: "))
    order_list.append(menu[choice-1])
    print("Your order is: ", order_list)
    for index, item in enumerate(order_list):
        print(index+1, item)
    want_more = input("Do you want to order more? (y/n): ")
    if want_more == "y":
        order(preference, order_list)
    else:
        print("Thank you for your order")
    
preference = input("Enter your preference (veg/non-veg): ")
order_list = []
order(preference, order_list)
"""
menu = {
    "veg": [
        {"name": "Veg Burger", "price": 90},
        {"name": "Veg Pizza", "price": 100},
        {"name": "Dosa", "price": 40},
    ],
    "non-veg": [
        {"name": "Chicken Burger", "price": 120},
        {"name": "Chicken Pizza", "price": 150},
        {"name": "Chicken Fry", "price": 80},
    ],
}


def order(preference, order_list):
    print("Menu: ")
    for index, dish in enumerate(menu[preference]):
        print(f"{index + 1}. {dish['name']} - {dish['price']}")
    try:
        choice = int(input("Enter your choice: "))
    except:
        print("Invalid input")
        exit()
    if choice > 3 or choice < 1:
        print("Invalid input")
        exit()
    order_list.append(menu[preference][choice - 1])
    print("Your order: ")
    for index, dish in enumerate(order_list):
        print(f"{index + 1}. {dish['name']} - {dish['price']}")
    want_more = input("Do you want to order more? (y/n): ")
    if want_more == "y":
        order(preference, order_list)
    else:
        total = 0
        for dish in order_list:
            total += dish["price"]
        print(f"Thank you for ordering. Your total bill is: Rs. {total}")


order_list = []

try:
    choice = int(input("1. Veg\n2. Non-Veg\n3. Exit\nEnter your preference: "))
    if choice == 3:
        print("Exiting")
        exit()
    choices = {1: "veg", 2: "non-veg"}
    preference = choices[choice]
    order(preference, order_list)
except:
    print("Invalid input")
    exit()
"""