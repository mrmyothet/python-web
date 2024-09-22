class Student:
    def __init__(self, name, age) -> None:
        self.name = name
        self.age = age

    def study(self):
        print(f"{self.name} is studying")


aung_aung = Student("Aung Aung", 20)
maung_maung = Student("Maung Maung", 22)
students = []
