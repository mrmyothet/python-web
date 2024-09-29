class User:
    def __init__(self, name, email) -> None:
        self.name = name
        self.email = email

class Student(User):
    def __init__(self, name, email, courses_enrolled) -> None:
        super().__init__(name, email)
        self.courses_enrolled = courses_enrolled

class Teacher(User):
    def __init__(self, name, email, courses_teached) -> None:
        super().__init__(name, email)
        self.courses_teached = courses_teached

class Course:
    def __init__(self, name, trainers, learners) -> None:
        self.name = name
        self.trainers = trainers
        self.learners = learners

python = Course("Python Crash Course", [], [])
dotnet = Course("C# DotNetCore", [], [])
docker = Course("Docker for Beginners", [], [])

courses = [python, dotnet, docker]

kyaw_kyaw = Student("kyaw_kyaw", "kyaw_kyaw@gmail.com", courses)

dotnet_trainer = Teacher("donet_trainer", "dotnet_trainer@gmail.com", [dotnet])
python_trainer = Teacher("python_trainer", "python_trainer@gmail.com", [python])
docker_trainer = Teacher("docker_trainer", "docker_trainer@gmail.com", [docker])

