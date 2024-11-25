### Define a base class
class Animal:
    def __init__(self, name): 
        self.name = name

    def speak(self):
        raise NotImplementedError("Subclass must implement this abstract method")
    

animal = Animal("Dog")
# print(animal)

# print(animal.speak())

class Dog(Animal):
    def speak(self):
        return self.name+' says Woof!'
    
dog = Dog("Dog")
print(dog.speak())

class Cat(Animal):
    def speak(self):
        return self.name+' says Meow!'
    
cat = Cat("Cat")
print(cat.speak())
    
