from sqlalchemy.orm import Session

from ..database.models.answer import Answer


def get_answer(db: Session, answer_id: int):
    return db.query(Answer).filter(Answer.answer_id == answer_id).first()


def create_attempt(db: Session, answer: Answer):
    db.add(answer)
    db.commit()
    db.refresh(answer)

    return answer
