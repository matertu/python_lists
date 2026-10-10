class Plant:
    def __init__(self, name: str, starting_height: float, starting_age: int):
        self.name = name
        self.starting_height = starting_height
        self.starting_age = starting_age

    def show(self) -> None:
            print(f"{self.name}: {self.starting_height:.1f}cm, {self.starting_age} days old")

def ft_plant_factory() -> None:
    rose = Plant("Rose", 25, 30)
    oak = Plant("Oak", 200, 365)
    cactus = Plant("Cactus", 5, 90)
    sunflower = Plant("Sunflower", 80, 45)
    fern = Plant("Fern", 15, 120)

    garden = [rose, oak, cactus, sunflower, fern]
    print("=== Plant Factory Output ===")
    for plant in garden:
        plant.show()

if __name__ == "__main__":
    ft_plant_factory()
