from itertools import combinations
from shapely import Polygon


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
    coords = [
        tuple([int(pt) for pt in line.strip().split(",")]) for line in data.splitlines()
    ]
    poly = Polygon(coords)
    candidate_polies = [
        ((abs(comb[0][0] - comb[1][0]) + 1) *
         (abs(comb[0][1] - comb[1][1]) + 1), comb)
        for comb in combinations(coords, 2)
    ]
    for candidate in sorted(candidate_polies, reverse=True):
        (size, (a, b)) = candidate
        candidate_poly = Polygon(
            [(a[0], a[1]), (a[0], b[1]), (b[0], b[1]), (b[0], a[1])])
        if candidate_poly.within(poly):
            return str(size)
