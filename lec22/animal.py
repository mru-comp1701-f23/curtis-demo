class Animal:
    def __init__(self, row: list) -> None:
        NAME = 0
        SPECIES = 1
        AGE_M = 2
        WEIGHT = 3
        ADOPTED = 4

        self.name = row[NAME]
        self.species = row[SPECIES]
        self.weight = row[WEIGHT]
        self.age = row[AGE_M]
        self.adopted = row[ADOPTED]
    
    def __str__(self) -> str:
        if self.adopted:
            return f"{self.name} the {self.species} has a new home!"
        else:
            return f"{self.name} the {self.species} is available for adoption"

if __name__ == "__main__":
    # testing animal stuff
    fido = Animal(["Fido", "dog", 12, 15.0, False])
    print(fido)
    fluffy = Animal(["Fluffy", "cat", 6, 3.5, True])
    print(fluffy)