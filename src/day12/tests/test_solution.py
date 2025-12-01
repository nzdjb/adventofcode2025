from pytest import fixture

from ..solution import solve_part1, solve_part2


@fixture
def part1_sample():
    data = """
"""
    expected = ""
    return [data, expected]


def test_solve_part1(part1_sample):
    (data, expected) = part1_sample
    assert solve_part1(data) == expected


@fixture
def part2_sample():
    data = """
"""
    expected = ""
    return [data, expected]


def test_solve_part2(part2_sample):
    (data, expected) = part2_sample
    assert solve_part2(data) == expected
