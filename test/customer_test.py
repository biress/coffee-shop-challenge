import pytest
from customer import Customer
from coffee import Coffee

def test_valid_customer():
    c = Customer("Alice")
    assert c.name == "Alice"

def test_invalid_name():
    with pytest.raises(ValueError):
        Customer("")

    with pytest.raises(ValueError):
        Customer("A" * 20)

def test_create_order_links():
    c = Customer("Bob")
    coffee = Coffee("Latte")
    c.create_order(coffee, 5.5)
    assert len(c.orders()) == 1
    assert coffee in c.coffees()
