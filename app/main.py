import logging
from fastapi import FastAPI
# from app.db.init_db import run_migrations

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)


app = FastAPI()

# run_migrations()

@app.get('/')
async def index():
    return {
        "message": "Welcome to the API. Use the `/docs` endpoint to access the API documentation."
    }
