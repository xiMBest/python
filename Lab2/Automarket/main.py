from Automobiles.Bmw import *
from Automobiles.Opel import *
from Automarket import *
from Automobiles.Man import *
from Automobiles.Nissan import *


if __name__ == '__main__':
    automarket = Automarket()

    bmw = Bmw(name='BMW')
    opel = Opel(name='Opel')
    nissan = Nissan(name='Nissan')
    man = Man(name='MAN')

    automarket.automobiles = [bmw, opel, man, nissan]
    print("Automobile list:")
    automarket.print_list()

    automarket.sort_by_engine()
    print("Sorted automobiles by engine")
    automarket.print_list()

    ls = automarket.find_by_engine(engine=2)
    print("Engine cars with 2 liters engine")
    for auto in ls:
        print(auto.name)
