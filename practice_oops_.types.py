# oops types
# Encapsulation
class BankAccount:        # the BankAccount class uses encapsulation to hide the balance variable from outside access
    def __init__(self, balance):
        self.__balance = balance

    def deposit(self, amount):   # The deposit methods provide a way to manipulate the balance variable while ensuring that it is always within a valid range. 
        self.__balance += amount

    def withdraw(self, amount):   # withdraw provide a way to manipulate the balance variable while ensuring that it is always within a valid range. 
        if amount <= self.__balance:
            self.__balance -= amount
        else:
            print("Insufficient balance")

    def get_balance(self):  # The get_balance method allows outside code to access the balance variable, but only in a controlled way.
        return self.__balance  
    
    # Inheritance:
    class Animal:   # Animal class defines common properties and methods that are shared by all animals.
     def __init__(self, name, age):
        self.name = name
        self.age = age

    def make_sound(self):
        pass

    class Dog(Animal):     # The Dog and Cat classes inherit from the Animal class and add their own unique make_sound methods.
     def make_sound(self):
        print("Woof!")

    class Cat(Animal):
      def make_sound(self):
        print("Meow!")

        # Polymorphism:
class Shape:
 def area(self):
          pass
class Rectangle(Shape):   # Shape class defines a common interface (area) that is shared by all shapes.
 def __init__(self, length, width):
  self.length = length
  self.width = width

def area(self):
 return self.length * self.width

class Circle(Shape):    # The Rectangle and Circle classes implement the area method in their own way, using different formulas to calculate the area based on their specific shapes.
         def __init__(self, radius):
          self.radius = radius

         def area(self):
          return 3.14 * (self.radius ** 2)
         
         # Abstraction:

         from abc import ABC, abstractmethod

         class Animal(ABC):
          @abstractmethod
          def make_sound(self):
           pass

         class Dog(Animal):
          def make_sound(self):
           print("Woof!")

         class Cat(Animal):
          def make_sound(self):
           print("Meow!")



