from pathlib import Path
from sys import argv


def load_input(input_file="input.txt") -> str:
    return (Path(argv[0]).parent / input_file).read_text()
