class Product:
    def __init__(self, code, name, price):
        self.code = code
        self.name = name
        self.price = price
    
    
    def __eq__(self, other):
        return (self.code == other.code and
        self.name == other.name and
        self.price == other.price
)