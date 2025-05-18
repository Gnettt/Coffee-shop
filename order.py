class Order:
    _all_orders = []

    def __init__(self, customer, coffee, price):
        self._customer = customer
        self._coffee = coffee
        if isinstance(price, float) and 1.0 <= price <= 10.0:
            self._price = price
        else:
            raise ValueError("Price must be a float between 1.0 and 10.0")

        Order._all_orders.append(self)
        print(f"Order created: {customer.name} ordered {coffee.name} for ${price:.2f}")

    def customer(self):
        return self._customer

    def coffee(self):
        return self._coffee

    def price(self):
        return self._price

    @classmethod
    def all(cls):
        print(f"Fetching all orders. Total: {len(cls._all_orders)}")
        return cls._all_orders
