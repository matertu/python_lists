def ft_count_harvest_recursive():
    limit = int(input("days until harvest: "))
    count_days(limit)
    print("Harvest time!")


def count_days(limit: int) -> None:
    if limit <= 0:
        return
    count_days(limit - 1)
    print(f"Day {limit}")
