items = {"Coffee": 7, "Pen": 3, "Paper cup": 2, "Milk": 1, "Coke": 4, "Book": 5}

while True:
    print("Select menu 1) check stock 2) warehousing 3) release 4) exit:")
    menu = input()

    if menu == "1":
        print("[Check stock] Enter item:")
        item = input()
        stock = items.get(item)
        if stock is not None:
            print("Stock:", stock)
        else:
            print("Item not found.")

    elif menu == "2":
        print("[Warehousing] Enter item and quantity:")
        item, quantity = input().split()
        quantity = int(quantity)
        items[item] = items.get(item, 0) + quantity
        print("Item added to inventory.")

    elif menu == "3":
        print("[Release] Enter item and quantity:")
        item, quantity = input().split()
        quantity = int(quantity)
        stock = items.get(item)
        if stock is not None:
            if stock >= quantity:
                items[item] -= quantity
                print("Item released from inventory.")
            else:
                print("Insufficient stock.")
        else:
            print("Item not found.")

    elif menu == "4":
        print("Program exited.")
        break

    else:
        print("Invalid menu selection. Please try again.")