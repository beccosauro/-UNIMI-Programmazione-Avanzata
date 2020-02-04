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

class ShapeIterator:
    def __init__(self, shapes):
        self._shapes = sorted(shapes,key = lambda x: x.calculate_area())
        self._index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self._index>=len(self._shapes): raise StopIteration
        actual = self._shapes[self._index]
        self._index+=1
        return actual

shapes=ShapeIterator([Square(6),Square(10),Square(5),Rectangle(12,4),Rectangle(12,12)])
iteratore = iter(shapes)
#for x in iteratore: print(x)

#Exercise 2: Playing around with Algebra. Non capisco l'algebra
import operator,functools,itertools
class Monoid:
    def __init__(self,elements,op):
        self._set = list(itertools.product(itertools.islice(elements,20),repeat=2))
        self._op =  { "+": operator.add, "*": operator.mul }[op]

    whole = property(lambda self: self._set)
    op = property(lambda self: self._op)  
    
    def getIdentity(self):
        
        whole = [self.whole[x:x+20] for x in range(0,len(self.whole),20)]
        print(whole)

        return list(map(lambda x:operator.is_(x[0],x[1]),whole))

monoide = Monoid([True,False],"+") 
print(monoide.getIdentity())       