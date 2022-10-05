from dish import Dish

pannkakor = Dish("Pannkakor", 80, "Vegetarian", 20  )
dish2 = Dish("Köttsoppa", 75, "Meat", 150  )
dish3 = Dish("Biff med bearnaise", 90, "Meat", 50  )

lunchDishes = [pannkakor, dish2, dish3]

print("VEGETARISK")
for dish in lunchDishes:
    if dish.GetType() == "Vegetarian":
        print(f"{dish.GetName()} {dish.GetPrice()} {dish.GetCalories()}")

print("KÖTT")
for dish in lunchDishes:
    if dish.GetType()== "Meat":
        print(f"{dish.GetName()} {dish.GetPrice()} {dish.GetCalories()}")

print("VEGANSK")
for dish in lunchDishes:
    if dish.GetType() == "Vegan":
        print(f"{dish.GetName()} {dish.GetPrice()} {dish.GetCalories()}")






