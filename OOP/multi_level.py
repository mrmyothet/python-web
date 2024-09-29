class Animal:
    def __init__(self, name) -> None:
        self.name = name

    def eat(self):
        print(self.name, "is eatting ")

    def sleep(self):
        print(self.name, "is sleeping")

    
class Elephant(Animal):
    def __init__(self, name, food) -> None:
        super().__init__(name)
        self.food = food

    def eat(self):
        print(self.name, "is eating", self.food)

class IndianElephant(Elephant):
    def __init__(self, name, food, is_dance):
        super().__init__(name, food)
        self.is_dance = is_dance
    
    def dance(self):
        if self.is_dance == True:
            print(self.name, "is dancing.")
        else:
            print(self.name, "is not able to dance.")

elephant_obj = Elephant("elephant", "sugarcant")
elephant_obj.eat()
elephant_obj.sleep()

mo_mo = IndianElephant("Mo Mo", "Sugarcane", True)
mo_mo.eat()
mo_mo.sleep()
mo_mo.dance()