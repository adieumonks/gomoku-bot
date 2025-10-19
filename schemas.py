from typing import Literal

from pydantic import BaseModel, Field, model_validator


MoveTuple = tuple[int, int]


class MoveRequest(BaseModel):
    board_size: int = Field(gt=0)
    board: list[list[int]]
    to_play: Literal["B", "W"]
    last_move: MoveTuple | None = None
    move_number: int = Field(ge=1)

    @model_validator(mode="after")
    def validate_board(self) -> "MoveRequest":
        size = self.board_size
        if len(self.board) != size:
            raise ValueError("board size does not match board_size")

        for row in self.board:
            if len(row) != size:
                raise ValueError("board must be square with length board_size")
            for value in row:
                if value not in (0, 1, 2):
                    raise ValueError("board values must be 0, 1, or 2")

        return self

    @model_validator(mode="after")
    def validate_last_move(self) -> "MoveRequest":
        if self.last_move is None:
            return self

        x, y = self.last_move
        if not (0 <= x < self.board_size and 0 <= y < self.board_size):
            raise ValueError("last_move must be inside the board")

        return self


class MoveResponse(BaseModel):
    move: MoveTuple

    @model_validator(mode="after")
    def validate_move(self) -> "MoveResponse":
        x, y = self.move
        if x < 0 or y < 0:
            raise ValueError("move coordinates must be non-negative")
        return self
