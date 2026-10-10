class Plant:
    def __init__(self, name: str, height: float, days: int, grow_rate: float):
        self.name = name
        self.height = height
        self.days = days
        self.grow_rate = grow_rate

    def show(self) -> None:
        print(f"{self.name}: {self.height:.1f}cm, {self.days} days old")

    def grow(self) -> float:
        self.height += self.grow_rate
        return self.grow_rate

    def age(self) -> None:
        self.days += 1

def main() -> None:
    rose = Plant("Rose", 25, 30, 0.8)
    print("=== Garden Plant Growth ===")
    rose.show()
    count = 0
    for day in range(1, 8):
        print(f"=== Day {day} ===")
        count += rose.grow()
        rose.age()
        rose.show()
    print(f"Growth this week: {count:.1f}cm")

if __name__ == "__main__":
    main()
