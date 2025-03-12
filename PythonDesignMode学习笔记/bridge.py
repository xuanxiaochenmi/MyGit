from abc import ABCMeta, abstractmethod


class Shape(metaclass=ABCMeta):
    def __init__(self, color):
        self.color = color
    @abstractmethod
    def draw(self):
        pass

class Color(metaclass = ABCMeta):
    @abstractmethod
    def paint(self,shape): 
        pass
    
class Red(Color):
    def paint(self,shape):
        print('%s %s'%(shape.__class__.__name__,self.__class__.__name__))
        pass

class Rectangle(Shape):
    def draw(self):
        print('画一个矩形')
        self.color.paint(self)

class Circe(Shape):
    def draw(self):
        print('画一个圆')
        self.color.paint(self)

d = Rectangle(Red())
d.draw()
