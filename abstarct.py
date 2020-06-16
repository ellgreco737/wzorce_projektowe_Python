from abc import ABC, abstractmethod


class Animal(ABC):
    def __init__(self, animal_name, age, weight):
        self.animal_name = animal_name
        self.age = age
        self.weight = weight

    @abstractmethod
    def animal_name_species(self):
        pass

    def introduce_yourself(self):
        print(
            f"Jestem {self.animal_name_species()}. Mam na imię {self.animal_name}, "
            f"mam {self.age} lat oraz ważę {self.weight} kg."
        )


class Elephant(Animal):
    def animal_name_species(self):
        return "Słoń"


class Lion(Animal):
    def animal_name_species(self):
        return "Lew"


class Parrot(Animal):
    def animal_name_species(self):
        return "Papuga"

if __name__ == '__main__':
    Dumboo = Elephant('bartek', 77, 6000)
    Simba = Lion('karol', 34, 250)
    Jago = Parrot('ara', 12, 20)

    Dumboo.introduce_yourself()
    Simba.introduce_yourself()
    Jago.introduce_yourself()