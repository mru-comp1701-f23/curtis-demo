from animal import Animal

def get_dogs(animals: list[Animal]) -> list[Animal]:
    dogs = []
    for animal in animals:
        if animal.species == "dog":
            dogs.append(animal)
    return dogs

def main() -> None:
    animals = []
    animal_records = [
        ["Fido", "dog", 12, 15.0, False],
        ["Fluffy", "cat", 6, 3.5, True],
        ["Spot", "dog", 24, 20.0, False],
        ["Mittens", "cat", 3, 1.2, False],
        ["Rover", "dog", 36, 30.0, True],
        ["Whiskers", "cat", 1, 0.5, False],
    ]
    for animal in animal_records:
        animals.append(Animal(animal))

    dogs = get_dogs(animals)
    print(dogs)

main()