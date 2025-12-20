from pytest import mark

from ..solution import solve_part1, solve_part2

part1_samples = [
    (
        """3-5
10-14
16-20
12-18

1
5
8
11
17
32""",
        "3",
    ),
    (
        """3-5
10-14
16-20
12-18

1""",
        "0",
    ),
    (
        """3-5
10-14
16-20
12-18

5""",
        "1",
    ),
    (
        """3-5
10-14
16-20
12-18

8""",
        "0",
    ),
    (
        """3-5
10-14
16-20
12-18

11""",
        "1",
    ),
    (
        """3-5
10-14
16-20
12-18

17""",
        "1",
    ),
    (
        """3-5
10-14
16-20
12-18

32""",
        "0",
    ),
]


@mark.parametrize("data,expected", part1_samples)
def test_solve_part1(data: str, expected: str):
    assert solve_part1(data) == expected


part2_samples = [
    ("1-3\n5-7\n\n0", "6"),
    ("1-3\n2-5\n\n0", "5"),
]


@mark.parametrize("data,expected", part2_samples)
def test_solve_part2(data: str, expected: str):
    assert solve_part2(data) == expected
