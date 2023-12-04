NAME = 0
SPECIES = 1
AGE_M = 2
WEIGHT = 3
ADOPTED = 4

def get_dogs(animals: list[list]) -> list[list]:
    dogs = []
    for animal in animals:
        if animal[SPECIES] == "dog":
            dogs.append(animal)
    return dogs

def main() -> None:
    animals = [
        ["Fido", "dog", 12, 15.0, False],
        ["Fluffy", "cat", 6, 3.5, True],
        ["Spot", "dog", 24, 20.0, False],
        ["Mittens", "cat", 3, 1.2, False],
        ["Rover", "dog", 36, 30.0, True],
        ["Whiskers", "cat", 1, 0.5, False],
    ]
    dogs = get_dogs(animals)
    print(dogs)

main()