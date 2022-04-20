from sqlalchemy.orm import Session

from ..database.models.attempt import Attempt


def get_attempt(db: Session, attempt_id: int):
    return db.query(Attempt).filter(Attempt.attempt_id == attempt_id).first()


def create_attempt(db: Session, attempt: Attempt):
    db.add(attempt)
    db.commit()
    db.refresh(attempt)

    return attempt
