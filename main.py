from dish import Dish, DishType

def PrintSubMenu(rubrik:str, type:DishType, dishlist:list):
    print(rubrik)
    for dish in dishlist:
        if dish.GetType() == type:
            print(f"{dish.GetName()} {dish.GetPrice()} {dish.GetCalories()}")

pannkakor = Dish("Pannkakor", 80, DishType.Vegatarian, 20 )
dish2 = Dish("Köttsoppa", 75, DishType.Meat, 150  )
dish3 = Dish("Biff med bearnaise", 90, DishType.Meat, 50  )
dish = Dish("Köttbullar", 100, DishType.Meat , 100)
lunchDishes = [pannkakor, dish2, dish3, dish]

PrintSubMenu("VEGETARISK", DishType.Vegatarian, lunchDishes)
PrintSubMenu("KÖTT", DishType.Meat, lunchDishes)
PrintSubMenu("VEGANSK", DishType.Vegan, lunchDishes)

# class PlayerPosition(Enum):
#     Goalie = 1,
#     Defence= 2,
#     Midfielder = 3,
#     Forward = 4

# class Player:
#     def __init__(self, namn, playerposition)    :
#         self.__namn = namn
#         self.__playerposition = playerposition

# zlatan = Player("Zlatan", PlayerPosition.Forward )        


