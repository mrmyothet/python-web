class Animal:
    def __init__(self, legs, blood_type) -> None:
        self.legs = legs
        self.blood_type = blood_type

    def sleep(self):
        print(self, "is sleeping")

    def walk(self):
        print(self, "is walking")

class Monkey(Animal):
    def __init__(self, legs, blood_type, food):
        super().__init__(legs, blood_type)
        self.food = food

    def dance(self):
        print(self, "is dancing.")

    def sleep(self):
        print("Monkey is sleeping.")

class Fish(Animal):
    def __init__(self, legs, blood_type, color):
        super().__init__(legs, blood_type)
        self.color = color

    def swim(self):
        print(self, "is swmimming.")

m_obj = Monkey(2, "warm blood", "banana")
f_obj = Fish(0, "cold_blood", "blue")

m_obj.walk()
m_obj.sleep()
m_obj.dance()

f_obj = Fish(0, "cold blood", "blue")
f_obj.walk()
f_obj.sleep()
f_obj.swim()

monkey_is_animal = isinstance(m_obj, Animal)
print(monkey_is_animal)

monkey_is_fish = isinstance(m_obj, Fish)
print(monkey_is_fish)

fish_is_animal = isinstance(f_obj, Animal)
print(fish_is_animal)