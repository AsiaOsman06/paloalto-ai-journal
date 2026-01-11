from fastapi import FastAPI

app = FastAPI() # it use it to create new app

@app.get("/") # it a path creater and defines a path
def read_root():
    return {"FastAPI is working"}
