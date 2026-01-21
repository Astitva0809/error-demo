from fastapi import FastAPI
import sentry_sdk

sentry_sdk.init(
    dsn="https://2f070d8a068deb7da71b50b48bad718e@o4510731654397952.ingest.us.sentry.io/4510731685396480",
    send_default_pii=True,
)

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Site is running"}

@app.get("/error")
def error():
    x = None
    return x.id  # intentional crash

@app.get("/home")
def home():
    return {"message": "Site is fast"}


