def solve_part1(data: str) -> str:
    total = 0
    candidate_ranges = data.split(",")
    for candidate_range in candidate_ranges:
        [start, end] = candidate_range.split("-")
        candidate_generator = range(int(start), int(end) + 1)
        for candidate in candidate_generator:
            str_candidate = str(candidate)
            if len(str_candidate) % 2 != 0:
                continue
            half = len(str_candidate) // 2
            if str_candidate[half:] == str_candidate[:half]:
                total += candidate
    return str(total)


def solve_part2(data: str) -> str:
    return ""
