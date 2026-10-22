class Plant:
    def __init__(self, name: str, height: float, age: int) -> None:
        self._initialized: bool = False
        self._name: str = name
        self._height: float = 0
        self._age: int = 0
        self.set_height(height)
        self.set_age(age)
        self._initialized = True

    def get_name(self) -> str:
        return self._name

    def get_height(self) -> float:
        return self._height

    def get_age(self) -> int:
        return self._age

    def set_height(self, height: float) -> None:
        if height < 0:
            if self._initialized:
                print(f"{self._name}: Error, height can't be negative")
                print("Height update rejected")
            return
        self._height = float(height)
        if self._initialized:
            print(f"Height updated: {self._height:.1f}cm")

    def set_age(self, age: int) -> None:
        if age < 0:
            if self._initialized:
                print(f"{self._name}: Error, age can't be negative")
                print("Age update rejected")
            return
        self._age = int(age)
        if self._initialized:
            print(f"Age updated: {self._age} days")

    def show(self) -> None:
        print(
            f"{self.get_name()}: "
            f"{self._height:.1f}cm, "
            f"{self.get_age()} days old"
        )


def main() -> None:
    print("=== Garden Security System ===")
    rose = Plant("Rose", 15, 10)
    print("Plant created: ", end="")
    rose.show()
    print()

    """change with valid values"""
    rose.set_height(25)
    rose.set_age(30)
    print()

    """change with invalid values (negative)"""
    rose.set_height(-1)
    rose.set_age(-1)

    print("\nCurrent state: ", end="")
    rose.show()


if __name__ == "__main__":
    main()
