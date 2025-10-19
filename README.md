# Gomoku Bot API

簡易的な五目並べ AI API を FastAPI で構築するリポジトリです。

## 前提

- Python 3.12
- [uv](https://github.com/astral-sh/uv) が利用可能であること

## ローカル起動

FastAPI アプリを `uv run uvicorn` で起動します。

```bash
uv run uvicorn main:app --host 127.0.0.1 --port 8000
```

## 動作確認

ヘルスチェックのエンドポイントに `curl` でアクセスします。

```bash
curl -s http://127.0.0.1:8000/healthz
```

`ok` が返れば起動確認は完了です。
