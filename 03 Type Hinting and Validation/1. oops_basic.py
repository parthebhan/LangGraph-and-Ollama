### 
# Define a base class
class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        raise NotImplementedError("Subclass must implement abstract method")

# Define a subclass
class Dog(Animal):
    def speak(self):
        return f"{self.name} says Woof!"

# Define another subclass
class Cat(Animal):
    def speak(self):
        return f"{self.name} says Meow!"

# Create instances of the subclasses
dog = Dog("Buddy")
cat = Cat("Whiskers")

# Call the speak method on each instance
print(dog.speak())  # Output: Buddy says Woof!
print(cat.speak())  # Output: Whiskers says Meow!