class Rectangle:
    def __init__(self,h,b):
        self._height = h
        self._width = b

    def calculate_area(self):
        return self._height*self._width

    def calculate_perimeter(self):
        return 2*(self._height+self._width)

    def __str__(self):
        return "I m a Rectangle! My sides are: {0}, {1}\nMy area is {2}".format(self._width,self._height, self.calculate_area())

class Square:
    def __init__(self,w):
        self._width = w

    def calculate_area(self):
        return self._width**2

    def calculate_perimeter(self):
        return 4*self._width

    def __str__(self):
        return "I m a Square! My side are: {0}\nMy area is {1}".\
        format(self._width, self.calculate_area())

shapes = [Square(6),Square(10),Square(5),Rectangle(12,4),Rectangle(12,12)]
shapes.sort(key = lambda x: x.calculate_area())
for x in shapes:print(x)