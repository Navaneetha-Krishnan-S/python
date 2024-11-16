

grocery_item = {}

def add_item(name,price):
    grocery_item[name]=price
    print(name," has been added to list, price is $ ",price )

def remove_item(name):
    if name in grocery_item:
        del grocery_item[name]
        print(name," has been removed.")
    else: 
        print("Item not in the list.")
def display_item():
    for item_name,item_price in grocery_item.items():
        print(item_name, " - ",item_price)

