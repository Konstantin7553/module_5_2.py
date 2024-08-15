class House:
    def __init__(self, name, number_of_floor):
        self.name = name
        self.number_of_floor = number_of_floor
        self.current_floor = 1
    def go_to(self, new_floor):
        if new_floor < 1 or new_floor > self.number_of_floor:
            print("Такого этажа не существует")
        else:
            for floor in range(1, new_floor + 1):
                print(floor)


    def __len__(self):
        return self.number_of_floor

    def __str__(self):
        return f"Название: {self.name}, кол-во этажей: {self.number_of_floor}"


my_house = House("ЖК Эльбрус", 30)
my_house1 = House("Домик в деревне", 3)


print(my_house)
print(my_house1)

print(len(my_house))
print(len(my_house1))







