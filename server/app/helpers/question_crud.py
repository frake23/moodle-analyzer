from sqlalchemy.orm import Session

from ..database.models.question import Question


def get_question_by_text(db: Session, text: str):
    return db.query(Question).filter(Question.text == text).first()


def create_question(db: Session, question: Question):
    if db_question := get_question_by_text(db, question.text):
        return db_question

    db.add(question)
    db.commit()
    db.refresh(question)

    return question
