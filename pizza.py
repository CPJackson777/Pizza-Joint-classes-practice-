# Make two different instances of a pizza. If you have properly defined the class, you should be able to do something like the following code with your Pizza type.

# meat_lovers = Pizza()
# meat_lovers.size = 16
# meat_lovers.style = "Deep dish"
# meat_lovers.add_topping("Pepperoni")
# meat_lovers.add_topping("Olives")
# meat_lovers.print_order()
# You should produce output in the terminal similiar to the following string.

# "I would like a 16-inch, deep-dish pizza with Pepperoni and Olives."

from classes import Pizza

sausage_pizza = Pizza("large", "thick")
buffalo_chicken_pizza = Pizza("medium", "thick")

# This is where I added toppings to the toppings list for the sausage pizza
sausage_pizza.add_topping("sausage")
sausage_pizza.add_topping("onions")

# This is where I added toppings to the toppings list for the buffalo chicken pizza
buffalo_chicken_pizza.add_topping("chicken")


# This is where I order the pizza
# I am calling my order_this_pizza function from my Pizza class
sausage_pizza.order_this_pizza(sausage_pizza.size, sausage_pizza.crust, sausage_pizza.toppings)

buffalo_chicken_pizza.order_this_pizza(buffalo_chicken_pizza.size,buffalo_chicken_pizza.crust, buffalo_chicken_pizza.toppings)

 


 