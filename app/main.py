import logging
from fastapi import FastAPI
from app.api.v1.endpoints import user as user_router
# from app.db.init_db import run_migrations

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)


app = FastAPI()

# run_migrations()

app.include_router(prefix="/api/v1", router=user_router.router, tags=["Users"])

@app.get('/')
async def index():
    return {
        "message": "Welcome to the API. Use the `/docs` endpoint to access the API documentation."
    }
