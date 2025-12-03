def solve_part1(data: str) -> str:
    total = 0
    for line in data.splitlines():
        battery_list = list(line)
        max_volts = sorted(battery_list[:-1])[-1]
        max_volts2 = sorted(battery_list[battery_list.index(max_volts)+1:])[-1]
        total += int(f"{max_volts}{max_volts2}")
    return str(total)


def solve_part2(data: str) -> str:
    return ""
