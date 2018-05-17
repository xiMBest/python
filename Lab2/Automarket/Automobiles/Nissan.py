from Automobiles.Automobile import *
from enums.EUStandart import *
from enums.Energy import *
from enums.Category import *


class Nissan(Automobile):

    def __init__(self, name="Nissan", year=2000, weigth=3500, engine=3, cargo=1000, passenger=9, category=Category.MINIVEN, eustandart=EUStandart.EURO3, energy=Energy.GAS):
        Automobile.__init__(self, name, year, weigth, engine, cargo, passenger)
        self.category = category
        self.eustandart = eustandart
        self.energy = energy

    def __str__(self):
        return "Name : " + str(self.name) + ", made in " + str(self.year) + ", weigth is " + str(self.weight) + ", engine capacity is " + str(self.engine) +", cargo is " + str(self.cargo) + ", passengers can be " + str(self.passenger) + ", category is " + str(self.category) + ", eustandart is " + str(self.eustandart) +", energy is "+ str(self.energy)
