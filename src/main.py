from fastapi import FastAPI
from src.journal import add_entry, get_summary
app = FastAPI() # it use it to create new app

@app.get("/") # it a path creater and defines a path
def read_root():
    return {"FastAPI is working"}
@app.post("/entry")
def create_entry(text: str):
    return add_entry(text)

# @app.get("/summary")
# def summary():
#     return get_summary()