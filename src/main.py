from fastapi import FastAPI

from routes import router

app = FastAPI(
    title="Smart Expense Tracker API",
    description="A REST API to manage personal expenses.",
    version="1.0.0",
)

app.include_router(router)


@app.get("/")
def root():
    return {
        "message": "Welcome to Smart Expense Tracker API",
        "docs": "/docs"
    }