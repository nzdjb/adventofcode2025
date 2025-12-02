from math import floor
from operator import add, sub
import re


def solve_part1(data: str) -> str:
    dial = 50
    zeroes = 0
    data = data.splitlines()
    for entry in data:
        m = re.match("(?P<direction>[RL])(?P<quantity>[0-9]+)", entry)

        op = sub if m["direction"] == "L" else add
        dial = op(dial, int(m["quantity"])) % 100
        if dial == 0:
            zeroes = zeroes + 1
    return str(zeroes)


def solve_part2(data: str) -> str:
    dial = 50
    zeroes = 0
    data = data.splitlines()
    for entry in data:
        m = re.match("(?P<direction>[RL])(?P<quantity>[0-9]+)", entry)

        op = sub if m["direction"] == "L" else add
        quan = int(m["quantity"])
        zeroes += floor(abs(op(dial, quan) / 100))
        if dial > 0 and op(dial, quan) <= 0:
            zeroes += 1
        dial = op(dial, quan) % 100

    return str(zeroes)
