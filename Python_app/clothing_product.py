from product import Product

class ClothingProduct(Product):
    def __init__(self, product_id, name, price, size, color):
        super().__init__(product_id, name, price)
        self.size = size
        self.color = color

    def display_info(self):
        super().display_info()
        print(f"Size: {self.size}")
        print(f"Color: {self.color}")
