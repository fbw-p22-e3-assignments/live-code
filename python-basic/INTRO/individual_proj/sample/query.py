"""Command line interface to query the stock.

To iterate the source data you can use the following structure:

for item in warehouse1:
    # Your instructions here.
    # The `item` name will contain each of the strings (item names) in the list.
"""

from data import warehouse1, warehouse2

# YOUR CODE STARTS HERE

# Get the user name
user_name = input("What is your name? ")
print("Hello, " + user_name + "!")
print("What would you like to do?")
print("1. List all items by the warehouse")
print("2 Search an item and place an order")
print("3. Exit")

while True:
    user_input = input("Enter a number: ")
    
#########################################
    if user_input == "1":
        print('')
        print("******************")
        print("Items in warehouse 1: ")
        print("******************")
        print('')
        for item in warehouse1:
            print('-', item)
        
        print('')
        print("******************")
        print("Items in warehouse 2: ")
        print("******************")
        print('')
        for item in warehouse2:
            print('-', item)
        print(f"Thank you for using our service, {user_name}!")
        break
#########################################

#########################################
    elif user_input == "2":
        item_name = input("What is the name of the item? ")
        amount_warehouse1 = warehouse1.count(item_name)
        amount_warehouse2 = warehouse2.count(item_name)
        if amount_warehouse1 > 0 and amount_warehouse2 == 0:
            print(f"Amount available in warehouse 1: {amount_warehouse1}")
            yes_no = input("Would you like to place an order? (y/n) ")
            if yes_no == "y":
                print(f"Thank you for placing an order for {item_name}!")
                break
        elif amount_warehouse1 == 0 and amount_warehouse2 > 0:
            print(f"Amount available in warehouse 2: {amount_warehouse1}")
            yes_no = input("Would you like to place an order? (y/n) ")
            if yes_no == "y":
                print(f"Thank you for placing an order for {item_name}!")
                break
        elif amount_warehouse1 > 0 and amount_warehouse2 > 0:
            warehouse_dict = {amount_warehouse1: "warehouse1", amount_warehouse2: "warehouse2"}
            print(f"Amount available: {amount_warehouse1 + amount_warehouse2}")
            print(f"Location: Both warehouses")
            maximum = max(amount_warehouse1, amount_warehouse2)
            sum_items = amount_warehouse1 + amount_warehouse2
            print(f"Maximum available: {maximum} in {warehouse_dict[maximum]}")
            yes_no = input("Would you like to place an order? (y/n) ")
            if yes_no == "y":
                order_amount = int(input("How many would you like to order? "))
                if order_amount > sum_items:
                    print("****************************************")
                    print(f"Sorry, we only have {sum_items} in stock.")
                    print("****************************************")
                    order_max = input("Would you like to order the maximum amount? (y/n) ")
                    if order_max == "y":
                        print(f"Thank you for placing an order for {sum_items} {item_name}!")
                        break
                    else:
                        print("Thank you for using our service!")
                        break
                else:
                    print(f"Thank you for placing an order for {order_amount} {item_name}!")
                    break
            else:
                print("No, Goodbye!")
                break
        elif amount_warehouse1 + amount_warehouse2 == 0:
            print("Amount available: 0")
            print("Sorry, we don't have that item in stock.")
            print(f"Thank you for using our service, {user_name}!")
            break

    elif user_input == "3":
        print("Exit")
        break
    else:
        print("****************************************")
        print(f"Sorry, {user_name}, {user_input} is not a valid option.")
        print("****************************************")
        break
