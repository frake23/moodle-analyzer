from sqlalchemy.orm import Session

from ..database.models.test_question import TestQuestion


def get_test_question(db: Session, test_id: int, question_id):
    return db.query(TestQuestion).filter(TestQuestion.test_id == test_id & TestQuestion.question_id == question_id).first()


def create_test_question(db: Session, test_question: TestQuestion):
    if db_test_question := get_test_question(db, test_question.test_id, test_question.question_id):
        return db_test_question

    db.add(test_question)
    db.commit()
    db.refresh(test_question)

    return test_question
