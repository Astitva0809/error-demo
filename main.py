from fastapi import FastAPI
import sentry_sdk

sentry_sdk.init(
    dsn="https://911b0f938801e4bd64ff19981af1cf2f@o4510731654397952.ingest.us.sentry.io/4510731655577600",
    # Add data like request headers and IP for users,
    # see https://docs.sentry.io/platforms/python/data-management/data-collected/ for more info
    send_default_pii=True,
)

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Site is running"}

@app.get("/error")
def error():
    x = None
    return x.id   # ❌ This will crash (intentional)
