from fastapi import FastAPI
import sentry_sdk

sentry_sdk.init(
    dsn="https://2f070d8a068deb7da71b50b48bad718e@o4510731654397952.ingest.us.sentry.io/4510731685396480",
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
@app.get("/sentry-debug")
async def trigger_error():
    division_by_zero = 1 / 0
