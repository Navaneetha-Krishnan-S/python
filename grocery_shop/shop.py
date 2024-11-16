import grocery_operation as go

print("WELCOME TO KRISH GROCERY SHOP")
print("-----------------------------")



while(True):
    print("-----------------------------")
    
    print("1. Show item")
    print("2. Add item ")
    print("3. Remove item")
    print("4. Total Amount")
    print("5. Exit")
    user_input = input("Choose the option: ")
    try:
        if user_input == "1":
            if not go.grocery_item:
                print("No item in the list ")
            else:
                print(go.display_item())
        elif user_input == "2":
            item_name = input("Enter the item name: ")
            item_price = int(input("Enter the item price: "))
            go.add_item(item_name,item_price)
        elif user_input == "3":
            item_name = input("Enter the item name: ")
            go.remove_item(item_name)
        elif user_input == "4":
            print("Total amount : $ ",sum(go.grocery_item.values()))
        elif user_input == "5":
            print("Thank you Visit Again")
            break
        else: 
            print ( " Invalid Option")
    except Exception as e :
        print("Enter valid option: ",e)