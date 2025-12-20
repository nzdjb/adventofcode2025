from functools import reduce
from itertools import groupby
from operator import add, mul
from re import sub

ops = {"+": add, "*": mul}


def solve_part1(data: str) -> str:
    equations = zip(
        *[
            sub(r" +", " ", line.strip()).split(" ")
            for line in data.splitlines()
            if line
        ]
    )

    return str(
        sum(
            [
                reduce(ops[equation[-1]], map(int, equation[:-1]))
                for equation in equations
            ]
        )
    )


def solve_part2(data: str) -> str:
    lines = data.splitlines()
    op_list = [ops[operator] for operator in lines[-1].split(" ") if operator]
    groups = groupby(
        zip(*[line for line in lines[:-1] if line]),
        lambda column: all(map(lambda item: item == " ", column)),
    )
    chunks = [list(group) for is_sep, group in groups if not is_sep]
    return str(
        sum(
            [
                reduce(op_list[i], [int("".join(num)) for num in chunk])
                for i, chunk in enumerate(chunks)
            ]
        )
    )
