# class Product:
#     def __init__(self, product_id, name, price):
#         self.product_id = product_id
#         self.name = name
#         self.price = price

#     def display_info(self):
#         print(f"Product ID: {self.product_id}")
#         print(f"Product Name: {self.name}")
#         print(f"Product Price: {self.price}")
class Product:
    def __init__(self, product_id, name, price):
        self.__product_id = product_id
        self.name = name
        self.price = price

    def get_product_id(self):
        return self.__product_id

    def set_product_id(self, new_id):
        self.__product_id = new_id

    def display_info(self):
        print(f"Product ID: {self.__product_id}")
        print(f"Product name: {self.name}")
        print(f"Product price: {self.price}")
