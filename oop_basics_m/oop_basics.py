# define a class with 1 constructor, 2 attributes, and 1 method
# initiate an object
# modify an attribute within a loop

class Dog:
    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age

    def bark(self):
        return f"{self.name} says woof!"
    
mydog = Dog("buddy", 5)
mydog.color = "brown"

for i in range(5):
    mydog.age += 1