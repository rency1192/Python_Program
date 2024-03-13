from electronic_product import ElectronicProduct
from clothing_product import ClothingProduct
from prettytable import PrettyTable
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

    def display_all_products(self):
        table = PrettyTable()
        table.field_names = ["Product ID", "Name", "Price", "Type"]
        for product_id, product in self.products.items():
            table.add_row([product_id, product.name, product.price, type(product).__name__])
        print("\nAll Products:") 
        print(table)
        
    def get_product(self, product_id):
        return self.products.get(product_id)
    
    def get_valid_product_id(self):
        while True:
            product_id = input("Enter product ID: ")
            if product_id in self.products:
                return product_id
            else:
                print("Invalid product ID. Please enter a valid one.")
