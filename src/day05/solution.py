def solve_part1(data: str) -> str:
    lines = data.splitlines()
    split = lines.index("")
    fresh = lines[:split]
    ingredients = map(lambda x: int(x), lines[split+1:])
    fresh_lists = []
    for fresh_line in fresh:
        fresh_lists.append([int(x) for x in fresh_line.split("-")])

    fresh_ingredients = 0
    for ingredient in ingredients:
        for fresh_list in fresh_lists:
            if ingredient >= fresh_list[0] and ingredient <= fresh_list[1]:
                fresh_ingredients += 1
                break

    return str(fresh_ingredients)


def solve_part2(data: str) -> str:
    lines = data.splitlines()
    split = lines.index("")
    fresh = lines[:split]

    ranges = [range(*x) for x in ((int(v) + i for i,
                                   v in enumerate(f.split("-"))) for f in fresh)]

    ranges.sort(key=lambda r: r.start)

    final_ranges = []
    while len(ranges) > 1:
        [first, second, *rest] = ranges
        if first.stop >= second.start:
            ranges = [range(first.start, max(
                [first.stop, second.stop])), *rest]
        else:
            final_ranges.append(first)
            ranges = [second, *rest]

    final_ranges.append(ranges[0])

    total = sum([len(r) for r in final_ranges])

    return str(total)
