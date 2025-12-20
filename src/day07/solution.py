from functools import cache


def solve_part1(data: str) -> str:
    split_count = 0
    grid = [list(line) for line in data.splitlines()]
    for y, line in enumerate(grid):
        for x, char in enumerate(line):
            if char == ".":
                if grid[y - 1][x] == "S" or grid[y - 1][x] == "|":
                    grid[y][x] = "|"
            elif char == "^":
                if grid[y - 1][x] == "|":
                    split_count += 1
                    grid[y][x - 1] = "|"
                    grid[y][x + 1] = "|"

    return str(split_count)


def solve_part2(data: str) -> str:
    grid = [list(line) for line in data.splitlines()]
    limit = len(grid)

    @cache
    def beam(y: int, x: int) -> int:
        if y >= limit:
            return 1
        if grid[y][x] == "^":
            return beam(y + 2, x - 1) + beam(y + 2, x + 1)
        return beam(y + 1, x)

    return str(beam(1, grid[0].index("S")))
