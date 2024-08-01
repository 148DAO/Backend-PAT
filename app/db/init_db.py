from sqlalchemy.orm import Session
from app.db.session import engine   
from app.db.base import Base

def init_db() -> None:
    from app.db.models import user

    Base.metadata.create_all(bind=engine)


if __name__ == "__name__":
    init_db()