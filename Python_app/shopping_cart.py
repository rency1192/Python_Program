from clothing_product import ClothingProduct
from prettytable import PrettyTable
from product_list import ProductList

class ShoppingCart:
    def __init__(self):
        self.items = []

    def add_item(self, product, quantity=1):
        if isinstance(product, ClothingProduct):
            size = input(f"Enter size for {product.name}: ")
            color = input(f"Enter color for {product.name}: ")
            product.size = size
            product.color = color
        self.items.append({"product": product, "quantity": quantity})
        print(f"Added {quantity} {product.name}(s) to the cart.")

    def clear_cart(self):
        self.items = []
        print("Cleared the entire cart.")

    def remove_item(self, product_id):
        for item in self.items:
            product = item["product"]
            if hasattr(product, "get_product_id") and callable(product.get_product_id):
                current_product_id = product.get_product_id()
            else:
                current_product_id = None

            if current_product_id == product_id:
                self.items.remove(item)
                print(f"Removed {product.name} from the cart.")
                return

        print(f"Product with ID {product_id} not found in the cart.")

    def update_item(self, product_id, new_quantity=None, new_size=None, new_color=None):
        for item in self.items:
            product = item["product"]
            if hasattr(product, "get_product_id") and callable(product.get_product_id):
                current_product_id = product.get_product_id()
            else:
                current_product_id = None

            if current_product_id == product_id:
                if new_quantity is not None and new_quantity != "":
                    # try:
                    #     new_quantity = int(new_quantity)
                    #     if new_quantity <= 0:
                    #         print("Quantity must be a positive integer. Item not updated.")
                    #         return
                    # except ValueError:
                    #     print("Invalid quantity. Item not updated.")


                    item["quantity"] = new_quantity
                
                if isinstance(item["product"], ClothingProduct):
                    if new_size is not None and new_size != "":
                        item["product"].size = new_size

                    if new_color is not None and new_color != "":
                        item["product"].color = new_color

                print(f"Updated details for {item['product'].name}.")
                return

        print(f"Product with ID {product_id} not found in the cart. Item not updated.")

    def view_cart(self):
        if not self.items:
            print("\nYour cart is empty.")
            return

        table = PrettyTable()
        table.field_names = ["Product ID", "Name", "Price", "Size", "Colour", "Quantity"]

        for item in self.items:
            product = item["product"]
            quantity = item["quantity"]

            if isinstance(product, ClothingProduct):
                table.add_row([product.get_product_id(), product.name, product.price, product.size, product.color, quantity])
            else:
                table.add_row([product.get_product_id(), product.name, product.price, "-", "-", quantity])

        print("\nAll Products in cart:")
        print(table)

    def generate_bill(self):
        print("\nGENERATING FINAL BILL...")
        total_price = 0
        table = PrettyTable()
        table.field_names = ["Name", "Price", "Quantity"]

        for item in self.items:
            product = item["product"]
            quantity = item["quantity"]
            subtotal = int(product.price) * int(quantity)
            total_price += subtotal

            table.add_row([product.name, product.price, quantity])

        print(table)
        print(f"\nTotal Price: ${total_price}")
        print("\nThank you for shopping with us!\n")

