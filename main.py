from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def root():
    response = {
        "Message": "This is Ordering API"
    }
    return response
