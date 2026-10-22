class Plant:
    def __init__(
        self,
        name: str,
        height: float,
        age: int,
        grow_rate: float
    ) -> None:
        self._initialized: bool = False
        self._name: str = name
        self._height: float = 0.0
        self._age: int = 0
        self._grow_rate: float = float(grow_rate)
        self.set_height(height)
        self.set_age(age)
        self._initialized = True

    def get_name(self) -> str:
        return self._name

    def get_height(self) -> float:
        return self._height

    def get_age(self) -> int:
        return self._age

    def get_grow_rate(self) -> float:
        return self._grow_rate

    def set_height(self, height: float) -> None:
        if height < 0:
            if self._initialized:
                print(f"{self._name}: Error, height can't be negative")
                print("Height update rejected")
            return

        self._height = float(height)
        if self._initialized:
            print(f"Height updated: {self.get_height():.1f}cm")

    def set_age(self, age: int) -> None:
        if age < 0:
            if self._initialized:
                print(f"{self._name}: Error, age can't be negative")
                print("Age update rejected")
            return

        self._age = int(age)
        if self._initialized:
            print(f"Age updated: {self.get_age()} days")

    def grow(self) -> None:
        self._height += self.get_grow_rate()

    def age_one_day(self) -> None:
        self._age += 1

    def show(self) -> None:
        print(
            f"{self.get_name()}: "
            f"{self._height:.1f}cm, "
            f"{self.get_age()} days old"
        )


class Flower(Plant):
    def __init__(
            self, name: str,
            height: float,
            age: int,
            grow_rate: float,
            color: str
            ) -> None:
        super().__init__(name, height, age, grow_rate)
        self.color: str = color
        self._bloomed: bool = False

    def bloom(self) -> None:
        self._bloomed = True

    def show(self) -> None:
        super().show()
        print(f" Color: {self.color}")
        if self._bloomed:
            print(f" {self.get_name()} is blooming beautifully!")
        else:
            print(f" {self.get_name()} has not bloomed yet")


class Tree(Plant):
    def __init__(
            self, name: str,
            height: float,
            age: int,
            grow_rate: float,
            trunk_diameter: float
            ) -> None:
        super().__init__(name, height, age, grow_rate)
        self.trunk_diameter: float = trunk_diameter

    def produce_shade(self) -> None:
        print(f"Tree {self.get_name()} now produces a shade of "
              f"{self._height:.1f}cm long and "
              f"{self.trunk_diameter:.1f}cm wide.")

    def show(self) -> None:
        super().show()
        print(f" Trunk diameter: {self.trunk_diameter:.1f}cm")


class Vegetable(Plant):
    def __init__(
            self, name: str,
            height: float,
            age: int,
            grow_rate: float,
            harvest_season: str) -> None:
        super().__init__(name, height, age, grow_rate)
        self.harvest_season: str = harvest_season
        self.nutritional_value: int = 0

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
