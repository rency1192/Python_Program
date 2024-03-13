from product import Product

class ElectronicProduct(Product):
    def __init__(self, product_id, name, price, warranty_period):
        super().__init__(product_id, name, price)
        self.warranty_period = warranty_period

    def display_info(self):
        super().display_info()
        print(f"Warranty Period: {self.warranty_period} months")
