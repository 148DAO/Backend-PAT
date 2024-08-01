from fastapi import FastAPI
from app.api.v1.endpoints import user as user_router


app = FastAPI()

app.include_router(user_router.router)

@app.get('/')
async def index():
    return {
        "message": "Welcome to the API. Use the `/docs` endpoint to access the API documentation."
    }