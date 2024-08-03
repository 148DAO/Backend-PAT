from fastapi import FastAPI
from app.db.init_db import init_database


def main():
    init_database()

    app = FastAPI()

    @app.get('/')
    async def index():
        return {
            "message": "Welcome to the API. Use the `/docs` endpoint to access the API documentation."
        }
        
    return app


app = main()
