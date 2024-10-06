class Product:
    def __init__(self, code, name, price)
        self.code = code
        self.name = name
        self.price = price
    
    #display_info
    def __str__(self):
        return f'Product code: {self.code} - Product name: {self.name} - Product price: {self.price}'
    
    def