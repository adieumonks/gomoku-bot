from fastapi import FastAPI

app = FastAPI()


@app.get("/healthz")
def health_check() -> str:
    return "ok"
