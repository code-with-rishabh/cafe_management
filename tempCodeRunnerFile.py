# #Define the menu of restaurant
# menu = {

#     'Pizza': 100,
#     'Pasta': 90,
#     # 'Burger': 70,
#     'Coffee': 80,
#     'Salad' : 50,
# }

# #Greet
# print("Welcome to the Resturant")
# print("Pizza: Rs100\nPasta: Rs90\nBurger: Rs70\nCoffee: Rs80\nSalad: Rs50")

# order_total =0
# #90 + 70 = 160

# item_1 = input("Enter the name of item you want to order = ")
# if item_1 in menu :
#     order_total += menu[item_1] #0 + 70
#     print(f"Your item {item_1} has been added to your order ")

# else:
#     print(f"Ordered item {item_1} is not availabe yet!")

#     another_order = input("Do you want to add another item? (Yes/No)")
#     if another_order =="Yes":
#         item_2 = input("Enter the name of second item = ")
#         if item_2 in menu:
#             order_total += menu[item_2]
#             print(f"Item {item_2} has been added to order")
#         else:
#             print(f"Ordered item {item_2} is not available!")
            
#             print(f"The total amount of items to pay is {order_total}")