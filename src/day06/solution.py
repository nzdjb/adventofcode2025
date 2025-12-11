from functools import reduce
from operator import add, mul
from re import sub

ops = {
    "+": add,
    "*": mul
}


def solve_part1(data: str) -> str:
    equations = zip(*[sub(r" +", " ", line.strip()).split(" ")
                      for line in data.splitlines() if line])

    return str(sum([reduce(ops[equation[-1]], map(int, equation[:-1])) for equation in equations]))


def solve_part2(data: str) -> str:
    return ""
