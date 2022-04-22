from sqlalchemy.orm import Session

from ..database.models.test import Test
from ..database.models.student import Student
from ..schemas.mapped_test_create import MappedTestCreate
from . import answer_crud, attempt_crud, group_crud, question_crud, student_crud, test_crud, test_question_crud, variant_crud


def create_test(db: Session, mapped_test: MappedTestCreate):
    test = test_crud.create_test(db, Test(**mapped_test.test.dict()))

