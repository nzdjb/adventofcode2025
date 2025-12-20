from pytest import mark

from ..solution import solve_part1, solve_part2

part1_samples = [
    (
        """162,817,812
57,618,57
906,360,560
592,479,940
352,342,300
466,668,158
542,29,236
431,825,988
739,650,466
52,470,668
216,146,977
819,987,18
117,168,530
805,96,715
346,949,466
970,615,88
941,993,340
862,61,35
984,92,344
425,690,689""",
        10,
        "40",
    )
]


@mark.parametrize("data,connections,expected", part1_samples)
def test_solve_part1(data: str, connections: int, expected: str):
    assert solve_part1(data, connections) == expected


part2_samples = [
    (
        """162,817,812
57,618,57
906,360,560
592,479,940
352,342,300
466,668,158
542,29,236
431,825,988
739,650,466
52,470,668
216,146,977
819,987,18
117,168,530
805,96,715
346,949,466
970,615,88
941,993,340
862,61,35
984,92,344
425,690,689""",
        "25272",
    )
]


@mark.parametrize("data,expected", part2_samples)
def test_solve_part2(data: str, expected: str):
    assert solve_part2(data) == expected
