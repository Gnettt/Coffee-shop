from order import Order

class Coffee:
    def __init__(self, name):
        if isinstance(name, str) and len(name) >= 3:
            self._name = name
        else:
            raise ValueError("Coffee name must be at least 3 characters.")

    @property
    def name(self):
        return self._name

    def orders(self):
        coffee_orders = [order for order in Order.all() if order.coffee() == self]
        print(f"{self.name} has {len(coffee_orders)} orders")
        return coffee_orders

    def customers(self):
        unique_customers = list(set(order.customer() for order in self.orders()))
        print(f"{self.name} has been ordered by {len(unique_customers)} unique customers")
        return unique_customers

    def num_orders(self):
        count = len(self.orders())
        print(f"{self.name} has been ordered {count} times")
        return count

    def average_price(self):
        orders = self.orders()
        if orders:
            average = sum(order.price() for order in orders) / len(orders)
            print(f"Average price of {self.name}: ${average:.2f}")
            return average
        else:
            print(f"No orders found for {self.name}")
            return 0.0
