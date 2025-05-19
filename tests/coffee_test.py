import pytest
from coffee import Coffee
from customer import Customer

def test_valid_coffee():
    c = Coffee("Espresso")
    assert c.name == "Espresso"

def test_invalid_name():
    with pytest.raises(ValueError):
        Coffee("A")

def test_order_aggregation():
    customer = Customer("Zoe")
    coffee = Coffee("Mocha")
    customer.create_order(coffee, 4.5)
    customer.create_order(coffee, 5.5)
    assert coffee.num_orders() == 2
    assert round(coffee.average_price(), 2) == 5.0
