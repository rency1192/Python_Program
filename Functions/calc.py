
def add(x,y):
   sum = x + y
   print("sum is : ", sum)




def sub(x,y):
   sum = x - y
   print("sub is : ", sum)




def mul(x,y):
   sum = x * y
   print("multiplication : ", sum)




def div(x,y):
   sum = x / y
   print("sum is : ", sum)




print("1. Addition ")
print("2. Subtraction ")
print("3. Multiplication ")
print("4. Division ")






H = int(input("enter the number you want to perform : "))
x = int(input("enter the value of X : "))
y = int(input("enter the value of Y : "))


if H == 1:
   add(x,y)


elif H == 2:
   sub(x,y)


elif H == 3:
   mul(x,y)


elif H == 4:
   div(x,y)


else:
   print("You've entered wrong choice")