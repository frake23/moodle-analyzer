from sqlalchemy.orm import Session

from ..models import Answer, Attempt, Group, Question, Student, TestQuestion, Test, Variant
from ..schemas.mapped_test_create import MappedTestCreate
from . import answer_crud, attempt_crud, group_crud, question_crud, student_crud, test_crud, test_question_crud, variant_crud


def init_test(db: Session, mapped_test: MappedTestCreate):
    test = test_crud.create_test(db, Test(**mapped_test.test.dict()))

    for mapped_attempt in mapped_test.attempts:
        group = group_crud.create_group(
            db,
            Group(**mapped_attempt.student.group.dict())
        )
        student = student_crud.create_student(db, Student(
            **mapped_attempt.student.dict(exclude={'group'}),
            group_id=group.group_id
        ))
        attempt = attempt_crud.create_attempt(db, Attempt(
            completion_date=mapped_attempt.completion_date,
            test_id=test.test_id,
            student_id=student.student_id
        ))

        for mapped_question in mapped_attempt.questions:
            question_type = mapped_question.type.value
            question = question_crud.create_question(
                db,
                Question(
                    **mapped_question.dict(exclude={'variants', 'type', 'answer'}),
                    type=question_type
                )
            )

            if mapped_question.variants:
                for mapped_variant in mapped_question.variants:
                    variant_crud.create_variant(db, Variant(
                        question_id=question.question_id,
                        text=mapped_variant.text
                    ))

            test_question_crud.create_test_question(db, TestQuestion(
                test_id=test.test_id,
                question_id=question.question_id
            ))
            answer_crud.create_answer(db, Answer(
                **mapped_question.answer.dict(),
                attempt_id=attempt.attempt_id,
                question_id=question.question_id
            ))

    return mapped_test
