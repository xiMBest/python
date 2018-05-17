from Automobiles.Automobile import *
from enums.EUStandart import *
from enums.Energy import *
from enums.Category import *


class Bmw(Automobile):

    def __init__(self, name="bmw", year=2016, weigth=2000, engine=2, cargo=400, passenger=3, category=Category.CAR, eustandart=EUStandart.EURO5, energy=Energy.GASOLINE):
        Automobile.__init__(self, name, year, weigth, engine, cargo, passenger)
        self.category = category
        self.eustandart = eustandart
        self.energy = energy

    def __str__(self):
        return "Name : " + str(self.name) + ", made in " + str(self.year) + ", weigth is " + str(self.weight) + ", engine capacity is " + str(self.engine) +", cargo is " + str(self.cargo) + ", passengers can be " + str(self.passenger) + ", category is " + str(self.category) + ", eustandart is " + str(self.eustandart) +", energy is "+ str(self.energy)
