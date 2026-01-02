def ft_plant_age():
    plants_age = int(input("Enter plant age in days: "))
    if plants_age > 60:
        print("Plant is ready to harvest!")
    else:
        print("Plant needs more time to grow.")
