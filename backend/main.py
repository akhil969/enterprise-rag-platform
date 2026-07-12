from fastapi import FastAPI

from backend.routes import documents, search

app = FastAPI(title="EKIP")

app.include_router(documents.router)
app.include_router(search.router)


@app.get("/")
def health():
    return {"status": "running"}