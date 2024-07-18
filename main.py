from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from src.routes.code import router as code_router
from dotenv import load_dotenv
import os

load_dotenv() 

def create_app() -> FastAPI:
  app = FastAPI()

  app.add_middleware(
    CORSMiddleware,
    allow_origins = os.getenv("ALLOWED_ORIGINS"),
    allow_credentials = True if os.getenv("ALLOWED_CREDENTIALS") == "true" else False,
    allow_methods = os.getenv("ALLOWED_METHODS"),
    allow_headers = os.getenv("ALLOWED_HEADERS"),
  )
  app.include_router(code_router, prefix="/api")

  return app

app = create_app()
