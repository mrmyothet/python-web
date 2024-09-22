class Person:
    def __init__(self, name, age, job, township, pin):
        self.name = name
        self.age = age
        self.job = job
        self.township = township
        self.pin = pin

    def walk(self):
        print(f"{self.name} is walking")

    def sleep(self):
        print(f"{self.name} is sleeping")

    def eat(self):
        print(f"{self.name} is eating")


myothet = Person(
    name="Myo Thet",
    age=38,
    job="Software Developer",
    township="South Okkalapa",
    pin="045218",
)

myothet.walk()
myothet.sleep()
myothet.eat()
