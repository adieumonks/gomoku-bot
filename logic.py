from collections.abc import Sequence


def choose_move(board: Sequence[Sequence[int]]) -> tuple[int, int]:
    for y, row in enumerate(board):
        for x, value in enumerate(row):
            if value == 0:
                return x, y

    raise ValueError("no legal moves available")
