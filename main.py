from fastapi import FastAPI, HTTPException

from logic import choose_move
from schemas import MoveRequest, MoveResponse

app = FastAPI()


@app.get("/healthz")
def health_check() -> str:
    return "ok"


@app.post("/move", response_model=MoveResponse)
def choose_next_move(payload: MoveRequest) -> MoveResponse:
    try:
        move = choose_move(payload.board)
    except ValueError as exc:
        raise HTTPException(status_code=400, detail=str(exc)) from exc

    return MoveResponse(move=move)
