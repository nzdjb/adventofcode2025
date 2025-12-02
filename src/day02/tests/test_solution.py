from pytest import mark

from ..solution import solve_part1, solve_part2

part1_samples = [
    (
        "11-22,95-115,998-1012,1188511880-1188511890,222220-222224,1698522-1698528,446443-446449,38593856-38593862,565653-565659,824824821-824824827,2121212118-2121212124",
        "1227775554",
    )
]


@mark.parametrize("data,expected", part1_samples)
def test_solve_part1(data: str, expected: str):
    assert solve_part1(data) == expected


part2_samples = [
    ("11-22", "33"),
    ("95-115", "210"),
    ("998-1012", "2009"),
    ("1188511880-1188511890", "1188511885"),
    ("222220-222224", "222222"),
    ("1698522-1698528", "0"),
    (
        "11-22,95-115,998-1012,1188511880-1188511890,222220-222224,1698522-1698528,446443-446449,38593856-38593862,565653-565659,824824821-824824827,2121212118-2121212124",
        "4174379265",
    ),
]


@mark.parametrize("data,expected", part2_samples)
def test_solve_part2(data: str, expected: str):
    assert solve_part2(data) == expected
