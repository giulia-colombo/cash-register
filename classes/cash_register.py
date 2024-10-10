from classes.inventory import Inventory
from fractions import Fraction
class CashRegister:
    '''Represents a cash register for processing transactions. 
    Handles adding products, calculating totals, and applying discounts.'''

    def __init__(self):
        '''Initializes a new CashRegister with an empty current order.'''
        self.current_order = {}
        self.current_order_value = 0
        self.inventory = Inventory()

    def add_product(self, given_product_name): 
        '''Adds a product to the current order. If product is already present, increases the corresponding quantity.'''
        found_product_info = self.inventory.retrieve_product(given_product_name)
        if found_product_info == None:
            return 

        if given_product_name not in self.current_order:
            self.current_order[given_product_name] = {
                "code": found_product_info["code"],
                "name": found_product_info["name"],
                "price": found_product_info["price"],
                "quantity": 1
            }
        else:
            self.current_order[given_product_name]["quantity"] +=1
 
    def apply_discount_greentea(self):
        '''Checks for green tea in the order. If appropriate, applies buy-one-get-one discount to green tea products.'''
        green_tea_value = 0
        if "green tea" not in self.current_order:
            return green_tea_value
        
        quantity = self.current_order["green tea"]["quantity"]
        price = self.current_order["green tea"]["price"]

        if quantity < 2:
            green_tea_value = price * quantity
        else:
            green_tea_value = price * quantity
            if quantity % 2 == 0:
                green_tea_value = green_tea_value/2
            else:
                green_tea_value = (green_tea_value/2) + price
        return green_tea_value

    def apply_discount_coffee(self, discount_coefficient =Fraction(2,3), discount_threshold=3):
        '''Checks for coffee in the order. If appropriate, applies discount to coffee products.'''
        coffee_value = 0

        if "coffee" not in self.current_order:
            return coffee_value
    
        quantity = self.current_order["coffee"]["quantity"]
        price = self.current_order["coffee"]["price"]

        if quantity < discount_threshold:
            coffee_value = price * quantity
        else:
            coffee_value = discount_coefficient * quantity * price
        return coffee_value
    
    def apply_discount_strawberries(self, discounted_price=4.50, discount_threshold=3):
        '''Checks for strawberries in the order. If appropriate, applies discount to strawberry products.'''
        strawb_value = 0
        strawb_full_price = self.inventory.product_catalog["strawberries"]["price"]

        if 'strawberries' not in self.current_order:
            return strawb_value

        quantity = self.current_order["strawberries"]["quantity"]
    
        if quantity < discount_threshold:
            strawb_value = strawb_full_price * quantity
        else:
            strawb_value = discounted_price * quantity
        return strawb_value

    def calculate_total(self): 
        '''Calculates total value of current order after applying appropriate product discounts'''
        subtotals = [
            self.apply_discount_coffee(), 
            self.apply_discount_greentea(), 
            self.apply_discount_strawberries()
            ]
        
        self.current_order_value = sum(subtotals)
        return self.current_order_value



