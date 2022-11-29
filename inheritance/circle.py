from math import pi

class Circle: 
    def __init__(self, radius=1.0, color='red'):
        self.__radius = radius
        self.__color = color

    def setRadius(self, radius):
        self.__radius = radius

    def setColor(self, color):
        self.__color = color

    def getRadius(self):
        return self.__radius

    def getColor(self):
        return self.__color

    def toString(self):
        return f'Radius : {self.getRadius()}, Color: {self.getColor()}'

    def getArea(self):
        return pi * (self.getRadius() ** 2)