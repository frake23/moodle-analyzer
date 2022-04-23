from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from ..enums import QuestionType
from ..schemas.question import QuestionItemResponse, QuestionResponse
from ..database.engine import get_db
from ..helpers import question_crud, answer_crud

router = APIRouter(
    prefix="/question",
    tags=["question"]
)


@router.get('/', response_model=list[QuestionItemResponse])
def get_questions(test_id: int | None = None, db: Session = Depends(get_db)):
    print(test_id)
    if test_id:
        return question_crud.get_questions_by_test_id(db, test_id)
    return question_crud.get_questions(db)


@router.get('/{question_id}', response_model=QuestionResponse)
def get_question(question_id: int, test_id: int | None = None, db: Session = Depends(get_db)):
    question = question_crud.get_question_by_id(db, question_id)
    stats = {}
    if question.type != QuestionType.Text.value:
        stats = answer_crud.get_answers_count(db, question, test_id)

    return QuestionResponse(
        text=question.text,
        type=question.type,
        stats=stats if len(stats.keys()) != 0 else None
    )
