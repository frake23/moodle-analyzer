from sqlalchemy.orm import Session
from sqlalchemy import func
from ..models import Answer, Attempt, Test, Question
from ..enums import QuestionType


def get_answer_column(question_type: str):
    match question_type:
        case QuestionType.Variant.value:
            return Answer.answer_variant
        case QuestionType.Text.value:
            return Answer.answer_text
        case QuestionType.Number.value:
            return Answer.answer_number


def get_answer(db: Session, answer_id: int):
    return db.query(Answer).filter(Answer.answer_id == answer_id).first()


def get_answers_count(db: Session, question: Question, test_id: int | None):
    col = get_answer_column(question.type)

    q = db.query(col, func.count(), Attempt, Test)
    if test_id:
        q = q.filter(Test.test_id == test_id)

    return {
        i[0]: i[1] for i in
        q
        .filter(Answer.attempt_id == Attempt.attempt_id)
        .filter(Attempt.test_id == Test.test_id)
        .filter(Answer.question_id == question.question_id)
        .group_by(Answer.answer_id, Attempt.attempt_id, Test.test_id, col)
        .order_by(col)
        .all()
    }


def create_answer(db: Session, answer: Answer):
    db.add(answer)
    db.commit()
    db.refresh(answer)

    return answer
