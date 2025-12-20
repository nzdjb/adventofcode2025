from functools import reduce
from itertools import combinations
from math import dist
from operator import mul


def complete_circuits(circuits):
    completed_circuits = []
    while len(circuits) > 0:
        first, circuits = [circuits[0], circuits[1:]]
        for circuit in circuits:
            if not first.isdisjoint(circuit):
                circuit.update(first)
                break
        else:
            completed_circuits.append(first)
    return completed_circuits


def solve_part1(data: str, connections: int = 1000) -> str:
    coords = [
        tuple([int(pt) for pt in line.strip().split(",")]) for line in data.splitlines()
    ]
    combs = [(dist(*comb), comb) for comb in combinations(coords, 2)]
    combs = map(
        lambda comb: comb[1], sorted(combs, key=lambda comb: comb[0])[:connections]
    )
    circuits = []
    for comb in combs:
        for circ in circuits:
            if comb[0] in circ or comb[1] in circ:
                circ.add(comb[0])
                circ.add(comb[1])
                break
        else:
            circuits.append(set(comb))

    completed_circuits = complete_circuits(circuits)
    return str(reduce(mul, sorted(map(len, completed_circuits))[-3:]))


def solve_part2(data: str) -> str:
    coords = [
        tuple([int(pt) for pt in line.strip().split(",")]) for line in data.splitlines()
    ]
    target_length = len(coords)
    combs = [(dist(*comb), comb) for comb in combinations(coords, 2)]
    combs = map(lambda comb: comb[1], sorted(combs, key=lambda comb: comb[0]))

    circuits = []
    output = ""
    for comb in combs:
        for circ in circuits:
            if comb[0] in circ or comb[1] in circ:
                circ.add(comb[0])
                circ.add(comb[1])
                break
        else:
            circuits.append(set(comb))
        # Not throughly happy with this as it raises the order too much.
        circuits = complete_circuits(circuits)
        if len(circuits[0]) == target_length:
            output = str(comb[0][0] * comb[1][0])
            break
    return output
