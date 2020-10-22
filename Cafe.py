# Cafe ordering app
# dictionary holds cafe item inventory and price (USD)
cafe_menu = {'coffee' :{'espresso': 1.5,
                        'americano': 2,
                        'caffe latte': 2.25,
                        'mocha': 2.25,
                        'cappucino': 2.5,
                        'macchiato': 2.5},
            'tea' :{'white tea': 1.5,
                    'green tea': 2,
                    'oolong tea': 2.25,
                    'black tea': 2.25,
                    'earl grey tea': 2.5,
                    'matcha tea': 2.5},
            'pastries':{'croissant': 5.5,
                         'cinnamon roll': 4.5,
                         'banana bread': 4.25,
                         'pumpkin bread': 3.75,
                         'sticky bun': 4.25,
                         'apple turnover': 3.75}}
print("Welcome to DataWork Cafe!")
see_menu = input("Would you like to see the menu? (Y/N) ")
if see_menu.lower() == 'y':
    for category, item_list in cafe_menu.items():
        print(f"\n{category.title()}:")
    for item, price in item_list.items():
        print(f"\t{item.title()}......${price:.2f}")
place_order = input("\nWould you like to place an order? (Y/N) ")
if place_order.lower() == 'n':
    ordering = False
else:
    ordering = True
user_order = {}
while ordering:
    requested_item = input("Please enter an item: ")
    requested_item = requested_item.lower()
    quantity = input("How many do you want? ")
    quantity = int(quantity)
no_inventory = []
for item_group in cafe_menu.values():
    if requested_item in item_group.keys():
        user_order[requested_item] = quantity
        no_inventory.append(0)
    else:
        no_inventory.append(1)
if sum(no_inventory) == len(no_inventory):
    print("The item that you requested is not on our menu.")
order_again = input("Would you like to order something else? (Y/N) ")  
if order_again.lower() == 'y':
    ordering = True
else:        
    ordering = False 
subtotal = 0       
print("\nOrder Summary:")       
print("---------------------------")      
for ordered_item, number_items in user_order.items():          
    print(f"{ordered_item.title()} (Qty: {number_items})")       
    for item_group in cafe_menu.values():                
        if ordered_item in item_group.keys():                 
            temp_price = item_group[ordered_item]
tax = subtotal * 0.06
grand_total = subtotal + tax
print("---------------------------")
print(f"Subtotal: ${subtotal:.2f}")
print(f"Sales tax: ${tax:.2f}")
print(f"\nTotal: ${grand_total:.2f}")
print("\nThank you for visiting DataWork Cafe!")