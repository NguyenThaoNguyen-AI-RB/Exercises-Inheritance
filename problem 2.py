class Animal:
    def __init__(self, name:str):
        self.name = name
    def get_name(self):
        return self.name
class Reptile (Animal):
    def __init__(self, name):
        super().__init__(name)
class Mammal (Animal):
    def __init__(self, name):
        super().__init__(name)
class lizard (Reptile):
    def __init__(self, name):
        super().__init__(name)
class snake (Reptile):
    def __init__(self, name):
        super().__init__(name)
class bear (Mammal):
    def __init__(self, name):
        super().__init__(name)
class gorilla (Mammal):
    def __init__(self, name):
        super().__init__(name)
mammal = Mammal("Stella")
print(mammal.__class__.__bases__[0].__name__)
print(mammal.name)
print(Animal.__name__)
lizard = lizard("John")
print(lizard.__class__.__bases__[0].__name__)
print(lizard.name)
print(Animal.__name__)