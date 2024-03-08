class PC:
   def fun1(self):
       print("This is PC class")


class Laptop(PC):
   def fun2(self):
       print("This is Laptop class inheriting PC class")


class Mouse(Laptop):
   def fun3(self):
       print("This is Mouse class inheriting Laptop class")


class Student(Mouse, Laptop):
   def fun4(self):
       print("This is Student class inheriting PC and Laptop")




obj = PC()
obj.fun1()
obj1 = Laptop()
obj1.fun2()
obj2 = Mouse()
obj2.fun3()
obj3 = Student()
obj3.fun4()
