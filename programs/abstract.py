# Python does not provide abstract classes.
# Python comes with a module that provides the base for defining Abstract Base classes(ABC) and that
# module name is ABC
'''An abstract class can be considered as a blueprint for other classes.
A class which contains one or more abstract methods is called an abstract class.
An abstract method is a method that has a declaration but does not have an implementation.

--->IMPORTANCE :While we are designing large functional units we use an abstract class.When we want to provide a
                common interface for different implementations of a component, we use an abstract class.'''
from abc import ABC, abstractmethod


class Polygon(ABC):

    def noofsides(self):
        pass

class Triangle(Polygon):

    def noofsides(self):
         print("I have 3 sides")


class Pentagon(Polygon):

    def noofsides(self):
        print("I have 5 sides")


class Hexagon(Polygon):

    def noofsides(self):
        print("I have 6 sides")


class Quadrilateral(Polygon):

    def noofsides(self):
        print("I have 4 sides")

k=  Quadrilateral()
k.noofsides()

p= Pentagon()
p.noofsides()

c = Hexagon()
c.noofsides()
'''--------------------------------------------------------------------------------------------------------------'''
from abc import ABC, abstractmethod


class R(ABC):
    def rk(self):
        pass


class K(R):
    def rk(self):
        print("subclass ")


r = K()
r.rk()

p= R()
p.rk()