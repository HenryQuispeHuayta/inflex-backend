from fastapi import FastAPI
from src.routes.code import router as code_router

def create_app() -> FastAPI:
    app = FastAPI()
    app.include_router(code_router, prefix="/api")

    return app

app = create_app()
