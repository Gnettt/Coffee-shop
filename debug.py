from customer import Customer
from coffee import Coffee
from order import Order

alice = Customer("Alice")
bob = Customer("Bob")


latte = Coffee("Latte")
espresso = Coffee("Espresso")

order1 = Order(alice, latte, 3.5)
order2 = Order(bob, espresso, 2.0)
order3 = Order(alice, espresso, 4.5)


all_orders = Order.all()

