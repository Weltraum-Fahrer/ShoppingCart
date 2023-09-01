class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity


class InventoryManager:
    def __init__(self):
        self.inventory = []

    def add_product(self, name, price, quantity):
        product = Product(name, price, quantity)
        self.inventory.append(product)
        print(f"{name} added to the inventory.")

    def update_product(self, name, price, quantity):
        for product in self.inventory:
            if product.name == name:
                product.price = price
                product.quantity = quantity
                print(f"{name} updated in the inventory.")
                return
        print(f"{name} not found in the inventory.")

    def search_product(self, name):
        for product in self.inventory:
            if product.name == name:
                print(f"Name: {product.name}, Price: {product.price}, Quantity: {product.quantity}")
                return
        print(f"{name} not found in the inventory.")

    def print_inventory(self):
        print("Inventory:")
        for product in self.inventory:
            print(f"Name: {product.name}, Price: {product.price}, Quantity: {product.quantity}")


def main():
    user_name = input('Enter your name: ')
    inventory_manager = InventoryManager()
    print("Welcome To The Inventory Management System" + " " + user_name + '!')
    while True:
        print("\nOptions:")
        print("1. Add Product")
        print("2. Update Product")
        print("3. Search Product")
        print("4. Print Inventory")
        print("5. Exit")

        choice = int(input("Enter your choice: "))

        if choice == 1:
            name = input("Enter product name: ")
            price = float(input("Enter product price: "))
            quantity = int(input("Enter product quantity: "))
            inventory_manager.add_product(name, price, quantity)
        elif choice == 2:
            name = input("Enter product name: ")
            price = float(input("Enter updated product price: "))
            quantity = int(input("Enter updated product quantity: "))
            inventory_manager.update_product(name, price, quantity)
        elif choice == 3:
            name = input("Enter product name to search: ")
            inventory_manager.search_product(name)
        elif choice == 4:
            inventory_manager.print_inventory()
        elif choice == 5:
            print("You are now exiting the inventory management system. Goodbye" + user_name + "!!!")
            break
        else:

            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
