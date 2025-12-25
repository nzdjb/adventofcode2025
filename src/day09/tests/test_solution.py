from pytest import mark

from ..solution import solve_part1, solve_part2

part1_samples = [
    (
        """7,1
11,1
11,7
9,7
9,5
2,5
2,3
7,3""",
        "50",
    ),
    ("1,1\n3,3\n1,5", "9"),
]


@mark.parametrize("data,expected", part1_samples)
def test_solve_part1(data: str, expected: str):
    assert solve_part1(data) == expected


part2_samples = [
    (
        """7,1
11,1
11,7
9,7
9,5
2,5
2,3
7,3""",
        "24",
    ),
]


@mark.parametrize("data,expected", part2_samples)
def test_solve_part2(data: str, expected: str):
    assert solve_part2(data) == expected
