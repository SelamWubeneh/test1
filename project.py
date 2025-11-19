
# 1. Vending Machine Program
# Build a program that:>>>> here is how you start the program "welcome to vending machine"
# Displays a list of snacks and drinks with item numbers and prices. >>> initialize menu(item number . (name,price)) , > then initialize cart[] to store the selected item.
# Asks the user to choose items by number in a loop.
# Keeps track of selected items and their prices.
# Ends when the user types “done”.
# Finally prints a receipt showing:
# List of selected items with prices
# Total cost


# print("Welcome to Vending Machine! ")
# menu = {
#     1: {"name": "cookie", "price": 1.75},
#     2: {"name": "energydrink", "price": 2.00},
#     3: {"name": "candy", "price": 1.00},
#     4: {"name": "water", "price": 2.00},
# }
# cart = []
# # Display menu
# for item_num, details in menu.items():
#     print(f"{item_num}. {details['name']} - ${details['price']:.2f}")
# print("========================\n")
# while True:
#     choice=input("Enter item number or done").lower()
#     if choice == "done":
#         break
#     if choice.isdigit():
#         item_num=int(choice)
#         if item_num in menu: 
#             cart.append(menu[item_num])
#             # print(f" added{menu[item_num]['name'] - menu[item_num]['price']}to cart")
#             print(f"added{menu[item_num]['name']} - ${menu[item_num]['price']:.2f} to cart")
#         else: 
#             print("invalid item number. please try again")
#     else:
#         print("invalid item number")
  
# print("\n====RECEIPT=====")
# total_sum = 0
# if cart:
#     for item in cart:
#         print(f"{item['name']:15} ${item['price']:.2f}")
#         total_sum += item['price']

#     print("---------------------")
#     print(f"{'TOTAL':15} ${total_sum:.2f}")
# else:
#     print("No item selected")
# print("\n Thank you")


# 2. Simple Grocery Cart Checkout
# Write a program that:
# Has a predefined dictionary of groceries with prices.
# Lets the user “add” items by typing their names.
# For each valid item, asks for the quantity.
# Keeps adding to the cart until the user types "checkout".
# Displays a final bill: each item, quantity, subtotal, and total.
# Skills practiced: dictionaries, 

# thr project question requires storing more than just the pric: itm_name, price, quantity,{"name":"milk", "price":3.25,"qty:2"} subtotal and maybe other features..
# if we only use "milk":3.25 you onl have the price, nothing else, there will be no clean way to access the other fields. but with nested dictionary you can add other informations later
# milk":{"price:1.00","stock":20,"organic":True ......} the structure can become more expandable

# simply this project question needs more than the price. we need to store structured data so we can print recipts, 
# handle quantities, and later add more informations.



print("welcome to our groceries checkout machine! ")

GROCERIES = {
    "milk":1.00,
    "egg":2.00,
    "apple":3.00,
    "Butter": 11.00, 
    "Carrots": 7.00 
}
cart= {}
while True:
    choice= input("Enter your item or type checkout to finish").lower()
    if choice == "checkout":
        break
    if choice in GROCERIES:
        qty_input = input(f"how many {choice} do you want? ")
    #     if qty_input.isdigit():
    #     qty_input= int(qty_input)
    #     if choice in cart: 
    #         cart[choice]+= qty_input
    #     else:
    #         cart[choice] = qty_input 
    # else:
    #     print("Invalid item")




            


        

   



