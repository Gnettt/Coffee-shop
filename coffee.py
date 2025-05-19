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
        prices = [order.price for order in self.orders()]
        return sum(prices) / len(prices) if prices else 0
        print(f"[DEBUG] Average price for {self.name}: ${avg:.2f}")
        