# Наследование

class Shape:
    def __init__(self, color):
        self.color = color
    
    def draw(self):
        print("Рисуем фигуру")

class Circle(Shape):
    def draw(self):
        print(f"Рисуем круг цвета {self.color}")

class Square(Shape):
    def draw(self):
        print(f"Рисуем квадрат цвета {self.color}")

class Triangle(Shape):
    def draw(self):
        print(f"Рисуем треугольник цвета {self.color}")

circle = Circle("красный")
square = Square("синий")
triangle = Triangle("зеленый")

circle.draw()
square.draw()
triangle.draw()
