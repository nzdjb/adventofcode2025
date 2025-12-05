def solve_part1(data: str) -> str:
    total = 0
    grid = [list(line) for line in data.splitlines()]
    y_max = len(grid)
    x_max = len(grid[0])
    for y in range(y_max):
        for x in range(x_max):
            open_count = 0
            if grid[y][x] == ".":
                continue
            ds = [(dx, dy) for dx in range(-1, 2)
                  for dy in range(-1, 2) if (dx, dy) != (0, 0)]
            coords = [tuple(map(lambda a, b: a + b, (x, y), d)) for d in ds]
            for coord in coords:
                (cx, cy) = coord
                if cy < 0 or cy >= y_max or cx < 0 or cx >= x_max or grid[cy][cx] == ".":
                    open_count += 1
            if open_count >= 5:
                total += 1
    return str(total)


def solve_part2(data: str) -> str:
    total = 0
    grid = [list(line) for line in data.splitlines()]
    y_max = len(grid)
    x_max = len(grid[0])
    while True:
        removing = []
        for y in range(y_max):
            for x in range(x_max):
                open_count = 0
                if grid[y][x] == ".":
                    continue
                ds = [(dx, dy) for dx in range(-1, 2)
                      for dy in range(-1, 2) if (dx, dy) != (0, 0)]
                coords = [tuple(map(lambda a, b: a + b, (x, y), d))
                          for d in ds]
                for coord in coords:
                    (cx, cy) = coord
                    if cy < 0 or cy >= y_max or cx < 0 or cx >= x_max or grid[cy][cx] == ".":
                        open_count += 1
                if open_count >= 5:
                    removing.append((y, x))

        if len(removing) > 0:
            total += len(removing)
            for (y, x) in removing:
                grid[y][x] = '.'
        else:
            break
    return str(total)
