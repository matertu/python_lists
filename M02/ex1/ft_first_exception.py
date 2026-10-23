def input_temperature(temp_str: str) -> int | None:
    try:
        temperature: int = int(temp_str)
        print(f"Temperature is now {temperature}°C")
        return temperature
    except ValueError as e:
        print(f"Caught input_temperature error: {e}")
        return None

def test_temperature():
    print("=== Garden Temperature ===")
    print()
    print("Input data is '25'")
    input_temperature("25")
    print()
    print("Input data is 'abc'")
    input_temperature("abc")
    print()
    print("All tests completed - program didn't crash!")

if __name__ == "__main__":
    """temperature: str = input("Input a temperature: ")
    input_temperature(temperature)"""
    test_temperature()

    
