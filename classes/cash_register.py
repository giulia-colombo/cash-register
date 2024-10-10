from classes.inventory import Inventory

class CashRegister:
    def __init__(self):

        self.current_order = {}
        self.current_order_value = 0
        self.inventory = Inventory()

    def add_product(self, given_product_name): 
        '''Adds a product to the current order. If product is already present, increases the corresponding quantity.'''
        # take the selected product 
        # check if a dictionary exists inside {current_order} with the same name
        found_product_info = self.inventory.retrieve_product(given_product_name)
        # if product doesn't exist at all, display error:
        if found_product_info == None:
            print("It looks like this product doesn't exist in our catalog. Please try with an existing product.")
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
        # return current_order

# TO DO refactor here other functions like calculate_certainproduct_value
# TO DO: check for missing keys
    def apply_discount_greentea(self):
        # check if theres green tea in current order
        green_tea_value = 0
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

# TO DO: put hardcoded value as arguments
    def apply_discount_coffee(self):
        #nb coefficient for coffee discount
        coffee_value = 0
        coffee_discount_coefficient = 0.66
        quantity = self.current_order["coffee"]["quantity"]
        price = self.current_order["coffee"]["price"]
        if quantity < 3:
            coffee_value = price * quantity
        else:
            coffee_value = coffee_discount_coefficient * quantity * price
        return coffee_value
    
# TO DO: put hardcoded value as arguments
    def apply_discount_strawberries(self):
        # set price of strawberries
        strawb_full_price = self.inventory.product_catalog["strawberries"]["price"]
        strawb_discounted_price = 4.50
        quantity = self.current_order["strawberries"]["quantity"]
        strawb_value = 0
        # if quantity < 3, calculate normal value
        if quantity < 3:
            strawb_value = strawb_full_price * quantity
        # if quantity >= 3, change price, calculate disc value
        else:
            strawb_value = strawb_discounted_price * quantity
        # return strawb value
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



