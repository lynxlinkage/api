import logging
from sqlalchemy.orm import Session

from app import crud
from app.schemas.user import UserCreate
from app.db.session import Base, engine, SessionLocal

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def init_db() -> None:
    db = SessionLocal()
    try:
        # Create tables
        Base.metadata.create_all(bind=engine)
        
        # Create initial superuser
        user = crud.get_user_by_username(db, username="admin")
        if not user:
            user_in = UserCreate(
                username="admin",
                email="admin@example.com",
                password="admin",
                is_superuser=True,
            )
            user = crud.create_user(db, user_in=user_in)
            logger.info(f"Admin user created with id: {user.id}")
        else:
            logger.info("Admin user already exists")
    finally:
        db.close()


def main() -> None:
    logger.info("Creating initial data")
    init_db()
    logger.info("Initial data created")


if __name__ == "__main__":
    main()