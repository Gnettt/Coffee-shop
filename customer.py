from order import Order

class Customer:
    def __init__(self, name):
        if isinstance(name, str) and 1 <= len(name) <= 15:
            self._name = name
        else:
            raise ValueError("Name must be 1–15 characters.")

    @property
    def name(self):
        return self._name

    def orders(self):
        customer_orders = [order for order in Order.all() if order.customer() == self]
        print(f"{self.name}'s orders: {len(customer_orders)} found")
        return customer_orders

    def coffees(self):
        unique_coffees = list(set(order.coffee() for order in self.orders()))
        print(f"{self.name} has ordered {len(unique_coffees)} unique coffees")
        return unique_coffees

    def create_order(self, coffee, price):
        print(f"{self.name} is creating an order for {coffee.name} at ${price:.2f}")
        return Order(self, coffee, price)

    @classmethod
    def most_aficionado(cls, coffee):
        from order import Order
        customers = {}
        for order in Order.all():
            if order.coffee() == coffee:
                customers[order.customer()] = customers.get(order.customer(), 0) + order.price()
        if customers:
            most_spent = max(customers, key=customers.get)
            print(f"{most_spent.name} spent the most on {coffee.name}: ${customers[most_spent]:.2f}")
            return most_spent
        else:
            print(f"No orders found for coffee: {coffee.name}")
            return None
