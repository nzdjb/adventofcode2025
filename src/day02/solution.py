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
    total = 0
    candidate_ranges = data.split(",")
    for candidate_range in candidate_ranges:
        [start, end] = candidate_range.split("-")
        candidate_generator = range(int(start), int(end) + 1)
        for candidate in candidate_generator:
            str_candidate = str(candidate)
            str_candidate_length = len(str_candidate)
            for group_size in range(1, (str_candidate_length // 2) + 1):
                num_groups = str_candidate_length // group_size
                if num_groups * group_size != str_candidate_length:
                    continue
                if str_candidate[:group_size] * num_groups == str_candidate:
                    total += candidate
                    break

    return str(total)
