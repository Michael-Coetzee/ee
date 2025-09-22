import httpx
import asyncio
import random
from fastapi import HTTPException, responses

# First, I'll implement the github client with proper error handling for prod. 

async def get_user_gists(user: str, max_retries: int = 3):
    async with httpx.AsyncClient() as client:
        for attempt in range(max_retries):
            try:
                response = await client.get(
                    f"https://api.github.com/users/{user}/gists",
                    timeout=10.0
                )
                response.raise_for_status()
                return response.json()
            except httpx.HTTPError:
                if attempt == max_retries - 1:
                    raise HTTPException(status_code=502, detail="GitHub API unavailable.")
                await asyncio.sleep((2 ** attempt) + random.random())

# The async context manager ensures proper connection cleanup, 
# and i'm adding error handling for production resilience

