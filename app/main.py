from fastapi import FastAPI
from .github_client import get_user_gists
from datetime import datetime, timezone


app = FastAPI(title="GitHub Gists API", version="0.1.0")


@app.get("/health")
async def health_check():
    return {
        "status": "healthy",
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "service": "gists-api"
    }

@app.get("/{user}")
async def get_gists(user: str):
    return await get_user_gists(user)

# The health endpoint is crucial for container orchestation and monitoring
# systems.

