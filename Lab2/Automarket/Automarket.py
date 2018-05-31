class Automarket:
    automobiles = []

    def __init__(self):
        pass

    def sort_by_engine(self):
        self.automobiles.sort(key=lambda automobile: automobile.engine)


    def find_by_engine(self, engine):
        found_automobile = []

        for automobile in self.automobiles:
            if automobile.engine == engine:
                found_automobile.append(automobile)

        return found_automobile

    def add_automobile(self, automobile):
        self.automobiles += automobile

    def print_list(self):
        for automobile in self.automobiles:
            print(automobile)
        print("\n")
