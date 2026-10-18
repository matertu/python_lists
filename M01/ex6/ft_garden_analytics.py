class Plant:
    class Statistics:
        def __init__(self) -> None:
            self._grow_calls: int = 0
            self._age_calls: int = 0
            self._show_calls: int = 0

        def increment_grow(self) -> None:
            self._grow_calls += 1

        def increment_age(self) -> None:
            self._age_calls += 1

        def increment_show(self) -> None:
            self._show_calls += 1

        def display(self) -> None:
            print(
                f"Stats: {self._grow_calls} grow, "
                f"{self._age_calls} age, "
                f"{self._show_calls} show"
            )

    def __init__(
        self, name: str, height: float, age: int, grow_rate: float
    ) -> None:
        self._name: str = name
        self._height: float = height
        self._age: int = age
        self._grow_rate: float = grow_rate
        self.stats: Plant.Statistics = self.Statistics()

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
        self._height += self.get_grow_rate()
        self.stats.increment_grow()

    def age(self, days: int = 1) -> None:
        self._age += days
        self.stats.increment_age()

    def show(self) -> None:
        print(
            f"{self.get_name()}: {self._height:.1f}cm, "
            f"{self.get_age()} days old"
        )
        self.stats.increment_show()

    @staticmethod
    def older_than_year(days: int) -> bool:
        return days > 365

    @classmethod
    def anonymus(cls) -> "Plant":
        return cls("Unknown plant", 0.0, 0, 0.0)


class Flower(Plant):
    def __init__(
        self,
        name: str,
        height: float,
        age: int,
        growth_rate: float,
        color: str,
    ) -> None:
        super().__init__(name, height, age, growth_rate)
        self.color: str = color
        self._bloomed: bool = False

    def bloom(self) -> None:
        self._bloomed = True

    def show(self) -> None:
        super().show()
        print(f"Color: {self.color}")
        if self._bloomed:
            print(f"{self._name} is blooming beautifully!")
        else:
            print(f"{self._name} has not bloomed yet")


class Tree(Plant):
    class Statistics(Plant.Statistics):
        def __init__(self) -> None:
            super().__init__()
            self._shade_calls: int = 0

        def increment_shade(self) -> None:
            self._shade_calls += 1

        def display(self) -> None:
            super().display()
            print(f"{self._shade_calls} shade")

    def __init__(
        self,
        name: str,
        height: float,
        age: int,
        growth_rate: float,
        trunk_diameter: float,
    ) -> None:
        super().__init__(name, height, age, growth_rate)
        self.trunk_diameter: float = trunk_diameter
        self.stats: Tree.Statistics = self.Statistics()

    def produce_shade(self) -> None:
        print(
            f"Tree {self._name} now produces a shade of "
            f"{self._height:.1f}cm long and "
            f"{self.trunk_diameter:.1f}cm wide."
        )
        self.stats.increment_shade()

    def show(self) -> None:
        super().show()
        print(f"Trunk diameter: {self.trunk_diameter:.1f}cm")


class Vegetable(Plant):
    def __init__(
        self,
        name: str,
        height: float,
        age: int,
        growth_rate: float,
        harvest_season: str,
    ) -> None:
        super().__init__(name, height, age, growth_rate)
        self.harvest_season: str = harvest_season
        self.nutritional_value: int = 0

    def grow(self) -> None:
        super().grow()

    def age(self, days: int = 1) -> None:
        super().age(days)
        self.nutritional_value += days

    def show(self) -> None:
        super().show()
        print(f"Harvest season: {self.harvest_season}")
        print(f"Nutritional value: {self.nutritional_value}")


class Seed(Flower):
    def __init__(
        self,
        name: str,
        height: float,
        age: int,
        growth_rate: float,
        color: str,
        seeds: int = 42,
    ) -> None:
        super().__init__(name, height, age, growth_rate, color)
        self._target_seeds: int = seeds
        self.seeds_count: int = 0

    def bloom(self) -> None:
        super().bloom()
        self.seeds_count = self._target_seeds

    def show(self) -> None:
        super().show()
        print(f"Seeds: {self.seeds_count}")


def show_plant_stats(plant: Plant) -> None:
    plant.stats.display()


def main() -> None:
    print("=== Garden statistics ===")
    print("=== Check year-old")
    print(f"Is 30 days more than a year? -> {Plant.older_than_year(30)}")
    print(f"Is 400 days more than a year? -> {Plant.older_than_year(400)}")
    print()

    print("=== Flower")
    rose = Flower("Rose", 15.0, 10, 8.0, "red")
    rose.show()
    print("[statistics for Rose]")
    show_plant_stats(rose)
    print("[asking the rose to grow and bloom]")
    rose.grow()
    rose.bloom()
    rose.show()
    print("[statistics for Rose]")
    show_plant_stats(rose)
    print()

    print("=== Tree")
    oak = Tree("Oak", 200.0, 365, 0.0, 5.0)
    oak.show()
    print("[statistics for Oak]")
    show_plant_stats(oak)
    print("[asking the oak to produce shade]")
    oak.produce_shade()
    print("[statistics for Oak]")
    show_plant_stats(oak)
    print()

    print("=== Seed")
    sunflower = Seed("Sunflower", 80.0, 45, 30.0, "yellow")
    sunflower.show()
    print("[make sunflower grow, age and bloom]")
    sunflower.grow()
    sunflower.age(20)
    sunflower.bloom()
    sunflower.show()
    print("[statistics for Sunflower]")
    show_plant_stats(sunflower)
    print()

    print("=== Anonymous")
    anonymous = Plant.anonymus()
    anonymous.show()
    print("[statistics for Unknown plant]")
    show_plant_stats(anonymous)


if __name__ == "__main__":
    main()
