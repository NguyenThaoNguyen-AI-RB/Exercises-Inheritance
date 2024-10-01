class Product:
    def __init__(self, name:str, price:float):
        self.name = name
        self.price = price
class Beverage(Product):
    def __init__(self, name:str, price:float, milliliters:float):
        super().__init__(name, price)
        self.milliliters = milliliters
class Food(Product):
    def __init__(self, name:str, price:float, grams:float):
        super().__init__(name, price)
        self.grams = grams
class HotBeverage(Beverage):
    pass
class ColdBeverage(Beverage):
    pass
class Coffee(HotBeverage):
    MILLILITERS = 50
    PRICE = 3.50
    def __init__(self, caffeine:float):
        self.caffeine = caffeine
class Tea(HotBeverage):
    pass
class MainDish(Food):
    pass
class Dessert(Food):
    def __init__(self, calories:float):
        self.calories = calories
class Starter(Food):
    pass
class Salmon(MainDish):
    GRAMS = 22
class Cake(Dessert):
    GRAMS = 250
    CALORIES = 1000
    PRICE = 5
class Soup(Starter):
    pass

product = Product("coffee", 2.5)
print(product.__class__.__name__)
print(product.name)
print(product.price)
beverage = Beverage("coffee", 2.5, 50)
print(beverage.__class__.__name__)
print(beverage.__class__.__bases__[0].__name__)
print(beverage.name)
print(beverage.price)
print(beverage.milliliters)
soup = Soup("fish soup", 9.90, 230)
print(soup.__class__.__name__)
print(soup.__class__.__bases__[0].__name__)
print(soup.name)
print(soup.price)
print(soup.grams)