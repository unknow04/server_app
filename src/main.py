from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def say_hello():
    return {"msg": "hello !"}
