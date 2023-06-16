class Person:
    def __init__(self, name):
        self.name = name
    
    def greet(self):
        print(f"Привет, меня зовут {self.name}")

class Student(Person):
    def greet(self):
        print(f"Привет, меня зовут {self.name}. Я студент")

class Teacher(Person):
    def greet(self):
        print(f"Привет, меня зовут {self.name}. Я преподаватель")

class Doctor(Person):
    def greet(self):
        print(f"Привет, меня зовут {self.name}. Я врач")

student = Student("Иван")
teacher = Teacher("Елена")
doctor = Doctor("Александр")

student.greet()
teacher.greet()
doctor.greet()
