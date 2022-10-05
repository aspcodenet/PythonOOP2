from enum import Enum

class DishType(Enum):
    Vegan = 1,
    Meat = 2,
    Vegatarian = 3
    
class Dish:
    def __init__(self, name:str, price:int, type:DishType, calories:int ):
        self.__Name = name 
        self.__Price = price
        self.__Type = type
        self.__Calories = calories
    def GetType(self) -> DishType:
        return self.__Type
    def GetName(self) -> str:
        return self.__Name
    def GetPrice(self) -> int:
        return self.__Price
    def GetCalories(self) -> int:
        return self.__Calories

