from pytest import mark

from ..solution import solve_part1, solve_part2

part1_samples = [(
    """987654321111111
811111111111119
234234234234278
818181911112111""",
    "357"
),
    ("987654321111111", "98"),
    ("811111111111119", "89"),
    ("234234234234278", "78"),
    ("818181911112111", "92"),
]


@mark.parametrize("data,expected", part1_samples)
def test_solve_part1(data: str, expected: str):
    assert solve_part1(data) == expected


part2_samples = []


@mark.parametrize("data,expected", part2_samples)
def test_solve_part2(data: str, expected: str):
    assert solve_part2(data) == expected
