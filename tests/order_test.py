import pytest
from customer import Customer
from coffee import Coffee
from order import Order

def test_valid_order():
    c = Customer("Alex")
    cf = Coffee("Cappuccino")
    o = Order(c, cf, 3.5)
    assert o.customer == c
    assert o.coffee == cf
    assert o.price == 3.5

def test_invalid_price():
    c = Customer("Liam")
    cf = Coffee("Flat White")
    with pytest.raises(ValueError):
        Order(c, cf, 20.0)

def test_type_validation():
    with pytest.raises(TypeError):
        Order("not-a-customer", Coffee("Latte"), 3.0)
