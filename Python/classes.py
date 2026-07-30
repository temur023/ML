class MyClass:
    car_invented = 1886 #class variable

    def __init__(self, model, year,color,for_sale):
        self.model = model
        self.year = year
        self.color = color
        self.for_sale = for_sale
    def print_values(self):
        print("Model:", self.model)
        print("Year:", self.year)
        print("Color:", self.color)
        print("For Sale:", self.for_sale)
    def drive(self):
        print(f"The {self.model} is driving.")
    def stop(self):
        print(f"The {self.model} has stopped.")