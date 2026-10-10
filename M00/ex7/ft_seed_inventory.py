def ft_seed_inventory(seed_type: str, quantity: int, unit: str) -> None:
    seed_type = seed_type.capitalize()
    print(f"{seed_type} seeds: ", end="")
    match unit:
        case "packets":
            print(f"{quantity} packets available")
        case "grams":
            print(f"{quantity} grams available")
        case "area":
            print(f"covers {quantity} square meters")
