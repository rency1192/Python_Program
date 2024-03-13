class Product:
    def __init__(self, product_id, name, price):
        self.product_id = product_id
        self.name = name
        self.price = price

    def display_info(self):
        print(f"Product ID: {self.product_id}")
        print(f"Product Name: {self.name}")
        print(f"Product Price: {self.price}")

class ElectronicProduct(Product):
    def __init__(self, product_id, name, price, warranty_period):
        super().__init__(product_id, name, price)
        self.warranty_period = warranty_period

    def display_info(self):
        super().display_info()
        print(f"Warranty Period: {self.warranty_period} months")

class ClothingProduct(Product):
    def __init__(self, product_id, name, price, size, color):
        super().__init__(product_id, name, price)
        self.size = size
        self.color = color

    def display_info(self):
        super().display_info()
        print(f"Size: {self.size}")
        print(f"Color: {self.color}")

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

    def view_cart(self):
        if not self.items:
            print("\nYour cart is empty.")
            return
        print("_______________________________")
        print("\nSHOPING CART:")
        print("_______________________________")
        total_price = 0
        for item in self.items:
            product = item["product"]
            quantity = item["quantity"]
            total_price += product.price * quantity

            print("\nItem Details:")
            product.display_info()
            print(f"Quantity: {quantity} - Subtotal: ${product.price * quantity}\n")

        print(f"\nTotal Price: ${total_price}")
        print("_______________________________")

    def generate_bill(self):
        print("_______________________________")
        print("\nGENERATING FINAL BILL...")
        print("_______________________________")
        total_price = 0
        for item in self.items:
            product = item["product"]
            quantity = item["quantity"]
            total_price += product.price * quantity

            print("\nItem Details:")
            product.display_info()
            if isinstance(product, ClothingProduct):
                print(f"Size: {product.size}")
                print(f"Color: {product.color}")
            print(f"Quantity: {quantity} - Subtotal: ${product.price * quantity}\n")

        print(f"\nTotal Price: ${total_price}")
        print("\nThank you for shopping with us!")
        print("_______________________________")

class ProductList:
    def __init__(self):
        self.products = {}

    def add_product(self, product_id, name, price, product_type, **kwargs):
        if product_id not in self.products:
            if product_type == "electronics":
                self.products[product_id] = ElectronicProduct(product_id, name, price, warranty_period=12)
            elif product_type == "clothing":
                self.products[product_id] = ClothingProduct(product_id, name, price, size="", color="")
            else:
                print(f"Invalid product type for {name}. Skipping.")
        else:
            print(f"Product with ID {product_id} already exists. Skipping.")

    def display_products(self, category):
        print(f"\n{category.capitalize()} Products:")
        for product_id, product in self.products.items():
            if isinstance(product, ClothingProduct) and category.lower() != 'clothing':
                continue
            elif isinstance(product, ElectronicProduct) and category.lower() != 'electronics':
                continue
            print(f"Product ID: {product_id}")
            print(f"{product.name} - Price: ${product.price}\n")

    def get_product(self, product_id):
        return self.products.get(product_id)

    def get_valid_product_id(self):
        while True:
            product_id = input("Enter product ID: ")
            if product_id in self.products:
                return product_id
            else:
                print("Invalid product ID. Please enter a valid one.")

def main():
    product_list = ProductList()
    shopping_cart = ShoppingCart()

    product_list.add_product("L001", "Laptop", 1200, "electronics")
    product_list.add_product("P001", "Smartphone", 500, "electronics")
    product_list.add_product("S001", "Men's Shirt", 30, "clothing")
    product_list.add_product("S002", "Women's Dress", 50, "clothing")
    product_list.add_product("E001", "Headphones", 100, "electronics")

    print("\nAll Products:")
    for product_id, product in product_list.products.items():
        print(f"Product ID: {product_id}")
        print(f"{product.name} - Price: ${product.price}\n")

    shopping = True

    while shopping:
        print("\nSelect a Category:")
        print("1. Male")
        print("2. Female")
        print("3. Electronics")
        print("4. View Cart")
        print("5. Finish Shopping")

        choice = input("Enter your choice (1-5): ")

        if choice in ['1', '2', '3']:
            product_list.display_products("male") if choice == '1' else product_list.display_products(
                "female") if choice == '2' else product_list.display_products("electronics")
            product_id = product_list.get_valid_product_id()

            quantity = int(input("Enter quantity: "))

            selected_product = product_list.get_product(product_id)
            if selected_product:
                shopping_cart.add_item(selected_product, quantity)
            else:
                print("Invalid product ID.")
        elif choice == '4':
            shopping_cart.view_cart()
        elif choice == '5':
            shopping_cart.generate_bill()
            continue_shopping = input("Do you want to continue shopping? (yes/no): ").lower()
            if continue_shopping != 'yes':
                shopping = False
        else:
            print("Invalid choice. Please enter a number between 1 and 5.")

if __name__ == "__main__":
    main()
