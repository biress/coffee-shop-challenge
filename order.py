class Order:
    """Represents an order placed by a customer for a specific coffee."""

    def __init__(self, customer, coffee, price):
        from customer import Customer
        from coffee import Coffee

        if not isinstance(customer, Customer):
            raise TypeError("customer must be a Customer instance")
        if not isinstance(coffee, Coffee):
            raise TypeError("coffee must be a Coffee instance")
        if not isinstance(price, float) or not (1.0 <= price <= 10.0):
            raise ValueError("Price must be a float between 1.0 and 10.0")

        self._customer = customer
        self._coffee = coffee
        self._price = price

    @property
    def customer(self):
        """Return the customer who placed this order."""
        return self._customer

    @property
    def coffee(self):
        """Return the coffee ordered."""
        return self._coffee

    @property
    def price(self):
        """Return the price of this order."""
        return self._price
