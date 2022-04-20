from ..schemas.test_create import TestCreate
from ..schemas.mapped_test_create import *


def map_test_create(test_create: TestCreate) -> MappedTestCreate:
    test = MappedTest(name=test_create.name, link=test_create.name)

    attempts = []
    for item in test.data[0]:
        student_second_name = item[0]
        student_first_name = item[1]
        group_name = item[3]
        student_email = item[6]
        student_username = item[7]
        attempt_completion_date_str = item[10]
        questions_str = item[13:]
        student = MappedStudent(first_name=student_first_name, secondName=student_second_name,
                                email=student_email, username=student_username)
        group = MappedGroup(name=group_name)
        questions = [MappedQuestion(item[j], item[j+1], item[j+2])
                     for j in range(0, len(questions_str), 3)]
        attempts.append(MappedAttempt(student, group, questions))

    return MappedTestCreate(test, attempts)
