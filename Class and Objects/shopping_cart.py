class Product:
    def __init__(self,name,price):
        self.name=name
        self.price=price

class Cart:
    def __init__(self):
        self.list=[]
    
    def add_item(self,product,quantity):
        self.list.append({"product": product , "Quantity": quantity})
        
    def total(self):
        total=sum(i["Quantity"]*i["product"].price  for i in self.list )
        print("Total:",total)


laptop=Product("laptop",50000)
phone=Product("phone",17500)

c=Cart()

c.add_item(laptop,2)
c.add_item(phone,2)
c.total()