from pytest import mark

from ..solution import solve_part1, solve_part2


part1_samples = [
    (
        """L68
L30
R48
L5
R60
L55
L1
L99
R14
L82""",
        "3",
    )
]


@mark.parametrize("data,expected", part1_samples)
def test_solve_part1(data: str, expected: str):
    assert solve_part1(data) == expected


part2_samples = [
    (
        """L68
L30
R48
L5
R60
L55
L1
L99
R14
L82""",
        "6",
    ),
    ("R1000", "10"),
    (
        """R40
L20""",
        "0",
    ),
    (
        """L40
L20""",
        "1",
    ),
]


@mark.parametrize("data,expected", part2_samples)
def test_solve_part2(data: str, expected: str):
    assert solve_part2(data) == expected
