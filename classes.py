# Create a Pizza type for representing pizzas in Python. Think about some basic properties that would define a pizza's values; things like size, crust type, and toppings would help. Define those in the __init__ method so each instance can have its own specific values for those properties.

# Add a method for interacting with a pizza's toppings, called add_topping.

# Add a method for outputting a description of the pizza (sample output below).


class Pizza:
    def __init__(self, size, crust):
        self.size = "large"
        self.crust = "thick"
        self.toppings = list()
    
    def add_topping(self):
        self.toppings.append(topping)

    def order_this_pizza(self):
        toppings = "and" .join(toppings)
        print(f'I want to order a {self.size}{self.crust} pizza with {self.sauce} sauce, and {self.toppings}. Now, make it snappy!')
