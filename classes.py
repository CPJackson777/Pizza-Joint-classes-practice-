# Create a Pizza type for representing pizzas in Python. Think about some basic properties that would define a pizza's values; things like size, crust type, and toppings would help. Define those in the __init__ method so each instance can have its own specific values for those properties.

# Add a method for interacting with a pizza's toppings, called add_topping.

# Add a method for outputting a description of the pizza (sample output below).

# Make two different instances of a pizza. If you have properly defined the class, you should be able to do something like the following code with your Pizza type.

# meat_lovers = Pizza()
# meat_lovers.size = 16
# meat_lovers.style = "Deep dish"
# meat_lovers.add_topping("Pepperoni")
# meat_lovers.add_topping("Olives")
# meat_lovers.print_order()
# You should produce output in the terminal similiar to the following string.

# "I would like a 16-inch, deep-dish pizza with Pepperoni and Olives."

class Pizza:
    def __init__(self, size):
        self.size = ""
        self.crust = ""
        self.sauce = ""
        self.toppings = ""
    
    def add_topping(self):
        self.sauce = sauce
        self.cheese = cheese
        self.meats = meats
        self.veggies = veggies

    def order_this_pizza(self):
        print(f'I want to order a {self.crust}{self.size} pizza with {self.sauce} sauce, and {self.toppings}. Now, make it snappy!')

pizza1 = Pizza()
pizza1.add_topping

pizza1.order_this_pizza()
