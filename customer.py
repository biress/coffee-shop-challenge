class Customer:
    """Represents a customer who can place coffee orders."""

    def __init__(self, name):
        self.name = name
        self._orders = []

    @property
    def name(self):
        """Get the customer's name."""
        return self._name

    @name.setter
    def name(self, value):
        """Set the customer's name, enforcing validation."""
        if isinstance(value, str) and 1 <= len(value) <= 15:
            self._name = value
        else:
            raise ValueError("Name must be a string between 1 and 15 characters.")

    def orders(self):
        """Return a list of this customer's orders."""
        return self._orders

    def coffees(self):
        """Return a unique list of coffees this customer has ordered."""
        return list(set(order.coffee for order in self._orders))

    def create_order(self, coffee, price):
        """Create a new order for a given coffee and price."""
        from order import Order
        order = Order(self, coffee, price)
        self._orders.append(order)
        coffee._orders.append(order)
        return order
