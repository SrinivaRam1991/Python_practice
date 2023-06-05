class Car:     # # Define a new class called Car
    def __init__(self, make, model, year):  # Define the __init__ method with three arguments: make, model, and year
        self.make = make        
        self.model = model
        self.year = year    #Assign the make, model, and year arguments to instance variables with the same names
    
    def get_make(self):   # Define a method called get_make that returns the value of the make instance variable

        return self.make
    
    def get_model(self):   # Define a method called get_model that returns the value of the model instance variable

        return self.model  
    
    def get_year(self):      # Define a method called get_year that returns the value of the year instance variable

        return self.year

car1 = Car("Toyota", "Camry", 2022)   # Create a new instance of the Car class with make "Toyota", model "Camry", and year 2022

print("Make:", car1.get_make())   # Print the make of car1 by calling the get_make method

print("Model:", car1.get_model())  # Print the model of car1 by calling the get_model method

print("Year:", car1.get_year())  # Print the year of car1 by calling the get_year method
