class Coffee:
    """Represents a coffee type offered in the shop."""

    def __init__(self, name):
        if isinstance(name, str) and len(name) >= 3:
            self._name = name
        else:
            raise ValueError("Coffee name must be a string with at least 3 characters.")
        self._orders = []

    @property
    def name(self):
        """Get the coffee's name."""
        return self._name

    def orders(self):
        """Return all orders placed for this coffee."""
        return self._orders

    def customers(self):
        """Return a unique list of customers who have ordered this coffee."""
        return list(set(order.customer for order in self._orders))

    def num_orders(self):
        """Return the number of times this coffee has been ordered."""
        return len(self._orders)

    def average_price(self):
        """Return the average price of all orders for this coffee."""
        if not self._orders:
            return 0
        return sum(order.price for order in self._orders) / len(self._orders)
