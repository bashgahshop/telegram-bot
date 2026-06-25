from fastapi import FastAPI, Request

app = FastAPI()

@app.get("/")
async def home():
    return {"status": "OK"}

@app.post("/")
async def telegram(request: Request):
    update = await request.json()
    print(update)
    return {"ok": True}