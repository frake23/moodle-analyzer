from sqlalchemy.orm import Session

from ..models import Question, TestQuestion, Test


def get_question_by_id(db: Session, question_id: int):
    return db.query(Question).filter(Question.question_id == question_id).first()


def get_question_by_text(db: Session, text: str):
    return db.query(Question).filter(Question.text == text).first()


def get_questions_by_test_id(db: Session, test_id: int):
    return db\
        .query(Question)\
        .filter(TestQuestion.test_id == Test.test_id)\
        .filter(TestQuestion.question_id == Question.question_id)\
        .filter(TestQuestion.test_id == test_id)\
        .all()


def get_questions(db: Session):
    return db.query(Question).all()


def create_question(db: Session, question: Question):
    if db_question := get_question_by_text(db, question.text):
        return db_question

    db.add(question)
    db.commit()
    db.refresh(question)

    return question
