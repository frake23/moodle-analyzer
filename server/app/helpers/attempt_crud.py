import datetime
from sqlalchemy.orm import Session

from ..database.models.attempt import Attempt


def get_attempt(db: Session, attempt_id: int):
    return db.query(Attempt).filter(Attempt.attempt_id == attempt_id).first()


def create_attempt(db: Session, item: list[list[str]], test_id: int, student_id: int):
    date = datetime.datetime()
    db_attempt = Attempt(completion_date=date, test_id=test_id, student_id=student_id)
    db.add(db_attempt)
    db.commit()
    db.refresh(db_attempt)

    return db_attempt
