
class Inventory:
    '''Represents an Inventory for storing current products and related information.. 
    Handles retrieving products.'''
    def __init__(self):
        '''Initializes a new Inventory with a set product catalog.'''
        self.product_catalog = {
            "coffee": {
                "code": "CF1",
                "name": "Coffee",
                "price": 11.23
            },
            "strawberries": {
                "code": "SR1",
                "name": "Strawberries",
                "price": 5
            },
            "green tea": {
                "code": "GR1",
                "name": "Green Tea",
                "price": 3.11
            }
        }


    def retrieve_product(self, given_product_name):
        '''Retrieves a product from the product catalog based on the user's input'''
        for product in self.product_catalog.keys():       
            if product == given_product_name:
                return self.product_catalog[product]
        return None
