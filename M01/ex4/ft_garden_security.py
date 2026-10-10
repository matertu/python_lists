class Plant:
    def __init__(self, name: str, height: float, age: int):
        self._name: str = name
        self._height: float = height
        self._age: int = age

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

    def show(self) -> None:
        print(f"{self.get_name()}: {self._height:.1f}cm, {self.get_age()} days old")

def main() -> None:
    print("=== Garden Security System ===")
    rose = Plant("Rose", 15, 10)
    print(f"Plant created: ", end="")
    rose.show()
    print()
    rose.set_height(25)
    rose.set_age(30)
    print()
    rose.set_height(-1)
    rose.set_age(-1)
    print(f"\nCurrent state: ", end="")
    rose.show()

if __name__ == "__main__":
    main()
