from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def instant():
    return {"message": "Hello World"}