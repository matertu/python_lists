class Plant:
    def __init__(self, name: str, height: float, age: int, grow_rate: float):
        self._name: str = name
        self._height: float = height
        self._age: int = age
        self._grow_rate = grow_rate

    def get_name(self) -> str:
        return self._name

    def get_height(self) -> float:
        return self._height

    def get_age(self) -> int:
        return self._age

    def set_height(self, height: float) -> None:
        if height < 0:
            print(f"{self._name}: Error, height can't be negative")
            print("Height update rejected")
        else:
            self._height = height
            print(f"Height updated: {self.get_height():.1f}cm")

    def set_age(self, age: int) -> None:
        if age < 0:
            print(f"{self._name}: Error, age can't be negative")
            print("Age update rejected")
        else:
            self._age = int(age)
            print(f"Age updated: {self.get_age()} days")

    def grow(self) -> None:
        self._height += self._grow_rate

    def show(self) -> None:
        print(f"{self.get_name()}: {self._height:.1f}cm, {self.get_age()} days old")
	

class Flower(Plant):
    def __init__(self, name: str, height: float, age: int, growth_rate: float, color: str) -> None:
        super().__init__(name, height, age, growth_rate)
        self.color = color
        self._bloomed = False

    def bloom(self) -> None:
        self._bloomed = True

    def show(self) -> None:
        super().show()
        print(f" Color: {self.color}")
        if self._bloomed:
            print(f" {self.name} is blooming beautifully!")
        else:
            print(f" {self.name} has not bloomed yet")


class Tree(Plant):
    def __init__(self, name: str, height: float, age: int, growth_rate: float, trunk_diameter: float) -> None:
        super().__init__(name, height, age, growth_rate)
        self.trunk_diameter = trunk_diameter

    def produce_shade(self) -> None:
        print(f"Tree {self.name} now produces a shade of "
              f"{self._height:.1f}cm long and "
              f"{self.trunk_diameter:.1f}cm wide.")

    def show(self) -> None:
        super().show()
        print(f" Trunk diameter: {self.trunk_diameter:.1f}cm")


class Vegetable(Plant):
    def __init__(self, name: str, height: float, age: int, growth_rate: float, harvest_season: str) -> None:
        super().__init__(name, height, age, growth_rate)
        self.harvest_season = harvest_season
        self.nutritional_value = 0

    def grow(self) -> None:
        super().grow()

    def age_one_day(self) -> None:
        super().age_one_day()
        self.nutritional_value += 1

    def show(self) -> None:
        super().show()
        print(f" Harvest season: {self.harvest_season}")
        print(f" Nutritional value: {self.nutritional_value}")


def main() -> None:
    print("=== Garden Plant Types ===")

    print("=== Flower")
    rose = Flower("Rose", 15.0, 10, 8.0, "red")
    rose.show()
    print("[asking the rose to bloom]")
    rose.bloom()
    rose.show()
    print()

    print("=== Tree")
    oak = Tree("Oak", 200.0, 365, 0.1, 5.0)
    oak.show()
    print("[asking the oak to produce shade]")
    oak.produce_shade()
    print()

    print("=== Vegetable")
    tomato = Vegetable("Tomato", 5.0, 10, 2.1, "April")
    tomato.show()
    print("[make tomato grow and age for 20 days]")
    for _ in range(20):
        tomato.grow()
        tomato.age_one_day()
    tomato.show()

if __name__ == "__main__":
    main()
