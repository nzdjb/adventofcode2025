from itertools import combinations
from math import dist


def solve_part1(data: str) -> str:
    coords = [
        tuple([int(pt) for pt in line.strip().split(",")]) for line in data.splitlines()
    ]
    sizes = [
        (abs(comb[0][0] - comb[1][0]) + 1) * (abs(comb[0][1] - comb[1][1]) + 1)
        for comb in combinations(coords, 2)
    ]
    return str(max(sizes))


def solve_part2(data: str) -> str:
    return ""
