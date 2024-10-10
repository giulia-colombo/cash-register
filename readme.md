# Cash Register

The Cash Register app is a command-line app that simulates a basic checkout experience at a store. It allows users to scan products, applies discount where the products are eligible for it and returns a total for check out.

## Features

- Scan products from a predefined inventory
- Automatically apply discounts based on the items in the cart
- Show the total price of the order
- Basic error handling for invalid products

## Table of Contents

1.  [Installation](#installation)
2.  [Usage](#usage)
3.  [Available Products](#available-products)
4.  [Discounts](#discounts)
5.  [Tests](#running-tests)
6.  [Documentation](#documentation)
7.  [Updates](#updates)

## Installation

To install and run this project locally, just clone the repository and navigate to the project directory.

No external dependencies are required.

## Usage

To start the application, simply execute `src/main.py`.

- The app will prompt you for a product name.
- Type the name of a product (e.g. `coffee`) to add it to cart.
- Enter `done` to complete scanning and get the total value of your order.
- Enter `exit` to leave the app at any moment.

## Available products

- Coffee
- Strawberries
- Green tea

You can extend the product catalog by adding new items in `Inventory` in the `inventory.py` file.

## Discounts

The app automatically applies the following discounts:

- Buy-one-get-one: for green tea.
- Discount on bulk quantities: for strawberres and coffee.

## Tests

Run `python -m unittest discover -s tests` to discover and run the tests in the `tests/` directory.

## Documentation

Here's a summary of the classes and methods used in the project:

### `Inventory` Class

Manages the existing products.

#### `product_catalog`

a dictionary that holds product details such as product code, name, and price.

#### `retrieve_product(given_product_name)`

retrieves a product with its detail from the catalog

- `given_product_name (str)`: name of the product to retrieve.
- returns: the found `product` (dictionary) or `None` if no match is found.

### `CashRegister` Class

Manages the order, applies discounts and calculates the total.

#### `current_order`

dictionary that keeps track of the products added to the cart and their quantities.

#### `current_order_value`

a numerical value representing the final, total cost of the order (after discounts).

#### `inventory`

an instance of Inventory, used to access product information.

#### `add_product (given_product_name)`

Adds a product to the current order. If the product is already in the order, its quantity is increased.

- `given_product_name ` (str): name of the product to be added.
- returns: nothing. Updates `self.current_order`.

#### `apply_discount_greentea(self)`

Applies a "buy-one-get-one-free" discount for green tea, every time 2 items of green tea are added to the cart.

- returns: `green_tea_value` (float): the total value of the green tea items after the discount is applied. If no discount is applied the value is calculated without a discount. If no green tea is in the order, the value will be 0.

#### `apply_discount_coffee(self, discount_coefficient=Fraction(2,3), discount_threshold=3)`

Applies a discount to coffee products if the quantity meets the discount threshold. The default discount reduces the total cost by 1/3 when buying 3 or more items.

- `discount_coefficient`: (Fraction): The fraction of the price applied as a discount (default is 2/3 of the total cost).
- `discount_threshold` (int): The minimum number of coffee items required to apply the discount (default is 3).
- Returns: `coffee_value` (float): the total value of the coffee items after the discount is applied. If no discount is applied the value is calculated without a discount. If no coffee is in the order, the value will be 0.

#### `apply_discount_strawberries(self, discounted_price=4.50, discount_threshold=3)`

Applies a discount to strawberries if the quantity meets the discount threshold. The discount reduces the unit price.

- `discounted_price` (float): discounted price per unit (default is 4.5.
- `discount_threshold` (int): The minimum number of strawberry items required to apply the discount (default is 3).
- Returns: `strawb_value` (float): the total value of the strawberry items after the discount is applied. If no discount is applied the value is calculated without a discount. If no straweberries are in the order, the value will be 0.

#### `calculate_total(self)`

Calculates the total value of the current order after applying all applicable product discounts.

- returns: `self.current_order_value` (float): the total value of the current order, which is made up of the sum of the subtotals for every product (including discounts).

### Utilities

#### `sanitize_user_input(input)`

Cleans user input by converting it to lowercase and removing extra spaces.

- `input` (str) : the input to be sanitized.
- returns: `sanitized_input` (str): the sanitized input.
