from circle import *

class Cylinder(Circle):
    def __init__(self, radius, color, height=1.0):
        super().__init__(radius, color)
        self.__height = height

    def setHeight(self, height):
        self.__height = height

    def getHeight(self):
        return self.__height

    def toString(self):
        return f'Radius : {self.getRadius()}, Color: {self.getColor()}, Height: {self.getHeight()}'

    def getVolume(self):
        return self.getArea() * self.getHeight()