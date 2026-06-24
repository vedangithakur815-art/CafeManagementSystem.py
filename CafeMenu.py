#define the Menu of the Restaurant
menu = {
    'Pizza':100,
    'Pasta':80,
    'Burger':60,
    'Coffee':70,
    'French Fries':70
}

#Greet
print("Welcome to Python Restaurant")
print("Pizza: Rs100\nPasta: Rs80\nBurger: Rs60\nCoffee: Rs70\nFrench Fries: Rs70")

order_total = 0

item_1 = input("Enter the name of the item you want to order = ")
if item_1 in menu:
    order_total += menu[item_1]
    print(f"Your item {item_1} has been added to your order")

else:
    print(f"Ordered item {item_1} is not available yet!")

another_order = input("Do you want to add another item ? (Yes/No) ")
if another_order == "Yes":
    item_2 = input("Enter the name of the second item = ")
    if item_2 in menu:
        order_total += menu[item_2]
        print(f"Item {item_2} has been added to your order")
    else:
        print(f"Ordered item {item_2} is not available!")

print(f"The total amount of item to pay is {order_total}")
