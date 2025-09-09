from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class RequestBody(BaseModel):
    name: str
    good_name: str

@app.get("/")
def health():
    return {"Hello": "World"}

@app.post("/")
def handle(data: RequestBody) -> dict:
    return {"hello": f"{data.name} your good name is {data.good_name}"}

if __name__ == "__main__":
    import uvicorn
    import os
    uvicorn.run(app, host="0.0.0.0", port=int(os.getenv("PORT", 8000)))
