from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Site is running"}

@app.get("/error")
def error():
    x = None
    return x.id   # ❌ This will crash (intentional)
