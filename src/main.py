from classes.cash_register import CashRegister
from classes.inventory import Inventory
from src.utils import sanitize_user_input

inventory = Inventory()
cash_register = CashRegister()

def main():
    print("Hi, welcome to our store. To scan an item, please enter the product name.")
    print("When you are finished scanning, please enter 'done'. Enter 'exit' at any time to leave.")
    while True:
        user_input = sanitize_user_input(input("Enter a product name: "))

        if user_input == "exit":
            print("Thank you for visiting us. See you soon.")
            break

        if user_input == "done":
            if not cash_register.current_order:
                print("Your cart is empty. If you wish to leave, please enter 'exit'. Otherwise, you can scan a product.")
                continue
            print("Hold on while I apply any discount and calculate your total.")
            order_value = cash_register.calculate_total()
            print(f"Your total today is {order_value}. Thank you for shopping with us.")
            break

        found_product = inventory.retrieve_product(user_input)
        if found_product == None:
            print("It looks like this product doesn't exist in our catalog. Please try with an existing product.")
        else:
            cash_register.add_product(user_input)
            print(f"1 ({user_input}) @ {found_product['price']} has been added to cart.")


if __name__ == "__main__":
    main()