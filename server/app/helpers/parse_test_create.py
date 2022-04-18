from sqlalchemy.orm import Session

from ..schemas.test_create import TestCreate
from . import test_crud


def init_test(db: Session, test: TestCreate):
    db_test = test_crud.create_test(db, test)

    for item in test.data:
        student_second_name = item[0]
        student_first_name = item[1]
        group_name = item[3]
        student_email = item[6]
        student_username = item[7]
        attempt_completion_date_str = item[10]

        questions = item[13:]
