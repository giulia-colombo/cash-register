from classes.product import Product

class Inventory:
    def __init__(self):
        self.product_catalog = [
            Product("GR1", "Green Tea", 3.11),
            Product("SR1", "Strawberries", 5.00),
            Product("CF1", "Coffee", 11.23)
        ]


    def retrieve_product(self, given_product_name):
        '''Retrieves a product from the product catalog based on the user's input'''
        for product in self.product_catalog:       

            if product.name == given_product_name:
                return product
        return None

    # TO DO
    def print_product_catalog(self):
        '''Prints out the current product catalog'''
        pass
