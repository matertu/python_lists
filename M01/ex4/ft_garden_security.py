class Plant:
    def __init__(self, name: str, starting_height: float, starting_age: int):
        self._name: str = name
        self._height: float = 0.0
        self._age: int = 0
        
        if starting_height < 0:
            print(f"{self._name}: Error, height can't be negative")
            print("Height update rejected")
        else:
            self._height = starting_height

        if starting_age < 0:
            print(f"{self._name}: Error, age can't be negative")
            print("Age update rejected")
        else:
            self._age = starting_age

    def get_name(self) -> str:
        return self._name

    def get_height(self) -> float:
        return self._height

    def get_age(self) -> int:
        return self._age

    def get_info(self) -> str:
        return f"{self._name}: {self._height:.1f}cm, {self._age} days old"

    def set_height(self, height: float) -> None:
        if height < 0:
            print(f"{self._name}: Error, height can't be negative")
            print("Height update rejected")
        else:
            self._height = height
            print(f"Height updated: {int(self._height) if self._height.is_integer() else self._height}cm")

    def set_age(self, age: int) -> None:
        if age < 0:
            print(f"{self._name}: Error, age can't be negative")
            print("Age update rejected")
        else:
            self._age = int(age)
            print(f"Age updated: {self._age} days")
