from classes.inventory import Inventory

class CashRegister:
    def __init__(self):

        self.current_order = {}
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

    # def apply_discount_coffee
    
    # def apply_discount_greentea
    # def apply_discount_strawberries

    # def calculate_total: sums value of products in the current order


