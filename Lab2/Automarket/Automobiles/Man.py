from Automobiles.Automobile import *
from enums.EUStandart import *
from enums.Energy import *
from enums.Category import *


class Man(Automobile):

    def __init__(self, name="MAN", year=2017, weigth=14000, engine=15, cargo=19000, passenger=2, category=Category.TRACK, eustandart=EUStandart.EURO6, energy=Energy.DIESEL):
        Automobile.__init__(self, name, year, weigth, engine, cargo, passenger)
        self.category = category
        self.eustandart = eustandart
        self.energy = energy

    def __str__(self):
        return "Name : " + str(self.name) + ", made in " + str(self.year) + ", weigth is " + str(self.weight) + ", engine capacity is " + str(self.engine) +", cargo is " + str(self.cargo) + ", passengers can be " + str(self.passenger) + ", category is " + str(self.category) + ", eustandart is " + str(self.eustandart) +", energy is "+ str(self.energy)
