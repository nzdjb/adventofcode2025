from pytest import mark

from ..solution import solve_part1, solve_part2

part1_samples = [("""
    123 328  51 64 
    45 64  387 23 
    6 98  215 314
    *   +   *   +  
""", "4277556")]


@mark.parametrize("data,expected", part1_samples)
def test_solve_part1(data: str, expected: str):
    assert solve_part1(data) == expected


part2_samples = []


@mark.parametrize("data,expected", part2_samples)
def test_solve_part2(data: str, expected: str):
    assert solve_part2(data) == expected
