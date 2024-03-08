class Person:
  
   def __init__(self, name, bdate, crnt_year):
       self.name = name
       self.bdate = bdate
       self.crnt_year = crnt_year
      
   def calculate_age(self):
       age = self.crnt_year - self.bdate
       return age


p1 = Person("Hetvi", 2002, 2024)
age = p1.calculate_age()
print(age)  # Printing the calculated age directly without passing 'self'


