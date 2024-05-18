import os


class Item:
    def __init__(self, name: str, price: int):
        self.name = name
        self.price = price


class ShoppingCart:
    def __init__(self):
        self.items = []

    def add(self, item: Item):
        """Add an item to the shopping cart."""
        self.items.append(item)
        print(f"{item.name} added to the shopping cart.")

    def total(self) -> int:
        """Calculate the total price of items in the shopping cart."""
        return sum(item.price for item in self.items)
    

    def item_count(self) -> int:
        """Return the number of items in the shopping cart."""
        return len(self.items)


if __name__ == '__main__':
    # Open output file for writing
    with open('output.txt', 'w') as output_file:
        num_items = int(input("Enter the number of items: "))
        items = []
        # Input items
        for _ in range(num_items):
            name, price = input("Enter item name and price separated by space: ").split()
            item = Item(name, int(price))
            items.append(item)

        # Initialize shopping cart
        cart = ShoppingCart()

        num_commands = int(input("Enter the number of commands: "))
        # Process commands
        for _ in range(num_commands):
            command = input("Enter command: ")
            if command == "len":
                output_file.write(f"Number of items in cart: {cart.item_count()}\n")
            elif command == "total":
                output_file.write(f"Total price of items: {cart.total()}\n")
            elif command == "add":
                item_name = input("Enter item name to add: ")
                item = next((item for item in items if item.name == item_name), None)
                if item:
                    cart.add(item)
                    output_file.write(f"Added {item_name} to cart.\n")
                else:
                    output_file.write(f"Item not found: {item_name}\n")
            else:
                output_file.write(f"Unknown command: {command}\n")
