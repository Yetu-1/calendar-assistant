from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.post("/assistant")
async def root():
    return {"response": "Hello from this side"}