"""
class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

p1 = Person("John", 36)

print(p1.name)
print(p1.age)
"""

"""class person:
	def __init__(self, age, name):
		self.name = name
		self.age = age

p = person(20, "shiv")
print(p.name)
print(p.age)"""

"""class person:
    def __init__(self, name, age) -> None:
        self.name = name
        self.age = age

    def __str__(self) -> str:
        return f"{self.name}({self.age})"
    
p = person("John", 22)
print(p)"""

"""class person:
    def __init__(self, name, age) -> None:
        self.name = name
        self.age = age
    def myfunc(self):
        print("Hello My name is "+self.name +"\nMy age is "+str(self.age))

p = person("John",22)
p.myfunc()"""

"""class fruits:
    def __init__(fruit, name, price) -> None:
        fruit.name = name
        fruit.price = price

    def fruit_func(fruit):
        print(f"The Fruit Name is {fruit.name} \n The Fruit Price is {fruit.price}")

fru = fruits("Apple", 30)
fru.fruit_func()
     """

"""class fruits:
    def __init__(self, name, price) -> None:
        self.name = name
        self.price = price
    
    def fruit_func(fruit):
        print("The Fruit Name is "+ fruit.name + "\n The price of fruit is "+ str(fruit.price))
    
fru = fruits("Orange", 20)

fru.price = 40

fru.fruit_func()"""

