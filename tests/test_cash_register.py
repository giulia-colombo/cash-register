import unittest
from classes.inventory import Inventory
from classes.cash_register import CashRegister
from fractions import Fraction

class TestCashRegister(unittest.TestCase):
    def setUp(self):
        self.cash_register = CashRegister()
        self.inventory = Inventory()
        self.products = self.inventory.product_catalog

    def test_add_product(self):
        initial_order = self.cash_register.current_order.copy()
        self.cash_register.add_product("banana")
        self.assertEqual(self.cash_register.current_order, initial_order)

        expected_current_order = {}
        for product_name, product_info in self.products.items():
            self.cash_register.add_product(product_name)

            expected_current_order[product_name] = {
                "code": product_info["code"],
                "name": product_info["name"],
                "price": product_info["price"],
                "quantity": 1
            }
            self.assertEqual( self.cash_register.current_order, expected_current_order )

        self.cash_register.add_product("coffee")
        expected_current_order["coffee"]["quantity"] +=1
        self.assertEqual(self.cash_register.current_order, expected_current_order)

    def test_apply_discount_greentea(self):
        green_tea_price = 3.11
        self.cash_register.current_order = {
            "green tea" : {
                "code": "GR1",
                "name": "Green Tea",
                "price": green_tea_price,
                "quantity": 4
            }
        }
        green_tea_discounted_value = self.cash_register.apply_discount_greentea()
        expected_green_tea_discounted_value = 6.22
        self.assertEqual(green_tea_discounted_value, expected_green_tea_discounted_value)

    def test_apply_discount_coffee(self):
        coffee_price = 11.23
        coffee_discount_coefficient = Fraction(2,3)
        self.cash_register.current_order = {
        "coffee" : {
        "code": "CF1",
        "name": "Coffee",
        "price": coffee_price,
        "quantity": 4
    }
}
        coffee_discounted_value = self.cash_register.apply_discount_coffee()
        expected_coffee_discounted_value = coffee_price * coffee_discount_coefficient * self.cash_register.current_order["coffee"]["quantity"]
        self.assertEqual(coffee_discounted_value, expected_coffee_discounted_value)



    def test_apply_discount_strawberries(self):
        strawb_full_price = 5.00
        strawb_discounted_price = 4.50

        self.cash_register.current_order = {
        "strawberries" : {
        "code": "SR1",
        "name": "Strawberries",
        "price": strawb_full_price,
        "quantity": 3
    }
}
        strawb_discounted_value = self.cash_register.apply_discount_strawberries()
        expected_strawb_discounted_value = self.cash_register.current_order["strawberries"]["quantity"] * strawb_discounted_price
        self.assertEqual(strawb_discounted_value, expected_strawb_discounted_value)

    def test_calculate_total(self):
        self.cash_register.current_order = {
        "coffee": {
            "code": "CF1",
            "name": "Coffee",
            "price": 11.23,
            "quantity": 3
        },
        "strawberries": {
            "code": "SR1",
            "name": "Strawberries",
            "price": 5,
            "quantity": 3
        },
        "green tea": {
            "code": "GR1",
            "name": "Green Tea",
            "price": 3.11,
            "quantity": 2
        }
    }
        self.cash_register.calculate_total()
        self.assertEqual(self.cash_register.current_order_value, 39.07)

        self.cash_register.current_order = {
            "green tea": {
                "code": "GR1",
                "name": "Green Tea",
                "price": 3.11,
                "quantity": 2
            }
        }
        self.cash_register.calculate_total()
        self.assertEqual(self.cash_register.current_order_value, 3.11)

        self.cash_register.current_order = {
            "strawberries": {
                "code": "SR1",
                "name": "Strawberries",
                "price": 5,
                "quantity": 3 
            },
            "green tea": {
                "code": "GR1",
                "name": "Green Tea",
                "price": 3.11,
                "quantity": 1
            }
        }
        self.cash_register.calculate_total()
        self.assertEqual(self.cash_register.current_order_value, 16.61 )

        self.cash_register.current_order = {
            "coffee": {
                "code": "CF1",
                "name": "Coffee",
                "price": 11.23,
                "quantity": 3
            },
            "strawberries": {
                "code": "SR1",
                "name": "Strawberries",
                "price": 5,
                "quantity": 1
            },
            "green tea": {
                "code": "GR1",
                "name": "Green Tea",
                "price": 3.11,
                "quantity": 1
            }
        }
        self.cash_register.calculate_total()
        self.assertEqual(self.cash_register.current_order_value, 30.57)


if __name__ == "__main__":
    unittest.main(verbosity=2)