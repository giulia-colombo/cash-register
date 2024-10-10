from classes.inventory import Inventory
from fractions import Fraction
class CashRegister:
    def __init__(self):

        self.current_order = {}
        self.current_order_value = 0
        self.inventory = Inventory()

    def add_product(self, given_product_name): 
        '''Adds a product to the current order. If product is already present, increases the corresponding quantity.'''
        # take the selected product 
        # check if a dictionary exists inside {current_order} with the same name
        print(f"LOG: ADD_PRODUCT called.")
        print(f"LOG: Attempting to retrieve product with name: {given_product_name} in order to add it to order.")
        found_product_info = self.inventory.retrieve_product(given_product_name)
        print(f"LOG: Retrieved product info: {found_product_info}")
        # if product doesn't exist at all, display error:
        if found_product_info == None:
            print("LOGS: product doesnt exist in catalog")
            return 
            # TO DO: plus here inventory.display_products ???

        # if product exists, but is not in current_order, create a dictionary for it inside current_order
        if given_product_name not in self.current_order:
            self.current_order[given_product_name] = {
                "code": found_product_info["code"],
                "name": found_product_info["name"],
                "price": found_product_info["price"],
                "quantity": 1
            }
        else:
            # if it does exist, access the found_product information
            # increase the quantity prop in that product's dictionary
            self.current_order[given_product_name]["quantity"] +=1
        print(f"LOG: Current order: {self.current_order}")
        # return current_order

# TO DO refactor here other functions like calculate_certainproduct_value
# TO DO: check for missing keys
    def apply_discount_greentea(self):
        print(f"LOG: calling APPLY_DISCOUNT_GREENTEA")
        green_tea_value = 0
        if "green tea" not in self.current_order:
            return green_tea_value
        
        quantity = self.current_order["green tea"]["quantity"]
        price = self.current_order["green tea"]["price"]
        print(f"LOG: ==> quantity: {quantity}, price: {price} ")

        
        if quantity < 2:
            green_tea_value = price * quantity
            print(f"LOG: green_tea_value ==>", green_tea_value)             
        else:
            green_tea_value = price * quantity
            print(f"LOG: green_tea_value ==>", green_tea_value)             
            if quantity % 2 == 0:
                green_tea_value = green_tea_value/2
                print(f"LOG: green_tea_value ==>", green_tea_value)
            else:
                green_tea_value = (green_tea_value/2) + price
                print(f"LOG: green_tea_value ==>", green_tea_value)
        return green_tea_value

# TO DO: put hardcoded value as arguments
    def apply_discount_coffee(self, discount_coefficient =Fraction(2,3), discount_threshold=3):
        print(f"LOG: calling APPLY_DISCOUNT_COFFEE")
        coffee_value = 0

        if "coffee" not in self.current_order:
            return coffee_value
    
        quantity = self.current_order["coffee"]["quantity"]
        price = self.current_order["coffee"]["price"]
        print(f"LOG: ==> quantity: {quantity}, price: {price} ")

        if quantity < discount_threshold:
            coffee_value = price * quantity
            print(f"LOG: coffee value ==> ", coffee_value)
        else:
            coffee_value = discount_coefficient * quantity * price
            print(f"LOG: coffee value ==> ", coffee_value)
        return coffee_value
    
# TO DO: put hardcoded value as arguments
    def apply_discount_strawberries(self, discounted_price=4.50, discount_threshold=3):
        print(f"LOG: calling APPLY_DISCOUNT_STRAWBS")
        strawb_value = 0
        strawb_full_price = self.inventory.product_catalog["strawberries"]["price"]
        print(f"LOG: strawb full price: {strawb_full_price}")

        if 'strawberries' not in self.current_order:
            return strawb_value

        quantity = self.current_order["strawberries"]["quantity"]
        print(f"LOG: quantity: {quantity}")
    
        # if quantity < 3, calculate normal value
        if quantity < discount_threshold:
            strawb_value = strawb_full_price * quantity
            print(f"LOG: strawb value: {strawb_value}")
        # if quantity >= 3, change price, calculate disc value
        else:
            strawb_value = discounted_price * quantity
            print(f"LOG: strawb value: {strawb_value}")
        # return strawb value
        return strawb_value

    def calculate_total(self): 
        '''Calculates total value of current order after applying appropriate product discounts'''
        subtotals = [
            self.apply_discount_coffee(), 
            self.apply_discount_greentea(), 
            self.apply_discount_strawberries()
            ]
        print(f"LOGS: subtotals: ==> ", subtotals )

        self.current_order_value = sum(subtotals)
        print(f"LOGS: current_order_value ==> ", self.current_order_value)

        return self.current_order_value



