from fastapi import FastAPI

app = FastAPI()

app.title = "Inflex API"

@app.get("/")
def read_root():
    return {"Hello": "World"}
