def ft_harvest_total():
    count = 0
    for i in range(1, 4):
        count += int(input(f"Day {i} harvest: "))
    print(f"Total hervest: {count}")
