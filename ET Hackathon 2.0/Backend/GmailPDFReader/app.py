from fastapi import FastAPI
from main import main

app = FastAPI()


@app.get("/")
def home():
    return {"status": "Gmail Sync Service Running"}


@app.post("/gmail/sync")
def sync_gmail():
    try:
        main()
        return {
            "success": True,
            "message": "Gmail Sync Completed"
        }
    except Exception as e:
        return {
            "success": False,
            "error": str(e)
        }