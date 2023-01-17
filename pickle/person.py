

class Person():
    def __init__(self,name, age):
        self.name = name
        try:
            self.age = int(age)
        except ValueError as e:
            print(e)
        
    def print_person(self):
        print(f"{self.name}{self.age}")
        
    def increse_age(self,years):
        try:
            self.age += int(years)
        except Exception as e:
            print(e)
        