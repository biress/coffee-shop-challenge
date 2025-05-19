from customer import Customer
from coffee import Coffee

def main():
    print("☕ Coffee Shop Debug Session ☕\n")

    # Create Customers
    alice = Customer("Alice")
    bob = Customer("Bob")
    print(f"Created customers: {alice.name}, {bob.name}")

    # Create Coffees
    latte = Coffee("Latte")
    espresso = Coffee("Espresso")
    print(f"Created coffees: {latte.name}, {espresso.name}")

    # Alice places some orders
    order1 = alice.create_order(latte, 4.5)
    order2 = alice.create_order(espresso, 5.0)

    # Bob places one order
    order3 = bob.create_order(latte, 3.75)

    print("\n--- Alice's Orders ---")
    for order in alice.orders():
        print(f"{order.coffee.name} - ${order.price}")

    print("\n--- Bob's Coffees ---")
    for coffee in bob.coffees():
        print(coffee.name)

    print("\n--- Coffee Statistics ---")
    print(f"{latte.name} - Orders: {latte.num_orders()}, Average Price: ${latte.average_price():.2f}")
    print(f"{espresso.name} - Orders: {espresso.num_orders()}, Average Price: ${espresso.average_price():.2f}")

    print("\n--- Customers per Coffee ---")
    print(f"{latte.name}: {[customer.name for customer in latte.customers()]}")
    print(f"{espresso.name}: {[customer.name for customer in espresso.customers()]}")

    print("\n✅ Debug session complete.\n")

if __name__ == "__main__":
    main()
