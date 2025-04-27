import time

menu = {
    "pepperoni": 799,
    "margherita": 699,
    "veggie": 749,
    "meat lovers": 999,
    "hawaiian": 899
}

payment_methods = ["cash on delivery", "online payment", "upi", "card payment"]

def order_pizza():

    print("\n\nWelcome to Yogesh Pizzas!")
    print("Here's our menu:")
    for item in menu:
        print(f"{item.title()} - Rs.{menu[item]}")
    print("\n\n")
   
    pizza_choice = input("What would you like to order? ").lower()

  
    while pizza_choice not in menu:
        pizza_choice = input("Sorry, we don't have that on our menu. Please choose something else: ").lower()

    payment_choice = input("How would you like to pay? ").lower()

    while payment_choice not in payment_methods:
        payment_choice = input("Sorry, we don't accept that payment method. Please choose something else: ").lower()

    total_cost = menu[pizza_choice]

 
    print("Generating receipt...")
    time.sleep(2)
    print("\n\n")
    print(f"You ordered a {pizza_choice.title()} pizza from Yogesh Pizzas for Rs.{menu[pizza_choice]}.")
    print(f"Your total cost is Rs.{total_cost}.")
    print(f"Payment method: {payment_choice.title()}.")
    print("Thank you for your order!")

order_pizza()
