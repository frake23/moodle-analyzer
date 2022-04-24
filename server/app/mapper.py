import re
from datetime import datetime
from .schemas.test import TestCreate
from .schemas.mapped_test_create import *
from .enums import QuestionType
from .enums import QuestionType
from .schemas.mapped_test_create import MappedVariant


months_dict = {'января': 1, 'февраля': 2, 'марта': 3, 'апреля': 4, 'мая': 5, 'июня': 6,
               'июля': 7, 'августа': 8, 'сентября': 9, 'октября': 10, 'ноября': 11, 'декабря': 12}

VARIANTS_REGEXP = r'\n[:;] (.*)'


def get_variants_sorted_text(s: str):
    return re.findall(r'.*\n: ', s)[0] + '\n; '.join(sorted(re.findall(VARIANTS_REGEXP, s)))


def str_to_date(s: str):
    date_items = s.split()
    time_items = date_items[3][1:].split(':')

    year = int(date_items[2])
    month = months_dict[date_items[1]]
    day = int(date_items[0])

    hour = int(time_items[0])
    minute = int(time_items[1])

    return datetime(year, month, day, hour, minute)


def get_question_type(strings: list[str]) -> QuestionType | None:
    if strings[2] == '-':
        return QuestionType.Text

    if len(re.findall(VARIANTS_REGEXP, strings[0])) != 0:
        return QuestionType.Variant

    try:
        float(strings[2])
        return QuestionType.Number
    except:
        return None


def get_variants(s: str) -> list[MappedVariant] | None:
    variants = list(map(lambda text: MappedVariant(
        text), re.findall(VARIANTS_REGEXP, s)))
    return variants if len(variants) != 0 else None


def get_answer(question_type: QuestionType, answer_str: str):
    if answer_str == '-':
        return MappedAnswer()
    match question_type:
        case QuestionType.Text:
            return MappedAnswer(answer_text=answer_str)
        case QuestionType.Number:
            return MappedAnswer(answer_number=float(answer_str))
        case QuestionType.Variant:
            return MappedAnswer(answer_variant=answer_str)


def map_test_create(test_create: TestCreate) -> MappedTestCreate:
    test = MappedTest(name=test_create.name, link=test_create.link)

    attempts = []
    for item in test_create.data[0]:
        student_second_name = item[0]
        student_first_name = item[1]
        group_name = item[3]
        student_email = item[6]
        student_username = item[7]
        attempt_completion_date = str_to_date(item[10])
        questions_str = item[13:]
        group = MappedGroup(name=group_name)
        student = MappedStudent(first_name=student_first_name, second_name=student_second_name,
                                email=student_email, username=student_username, group=group)
        questions = []
        for i in range(0, len(questions_str), 3):
            question_text = questions_str[i]
            question_type = get_question_type(questions_str[i:i+3])

            if question_type == QuestionType.Variant:
                question_text = get_variants_sorted_text(question_text)

            variants = get_variants(item[i])
            answer = get_answer(question_type, questions_str[i+1])
            question = MappedQuestion(
                text=question_text, type=question_type, variants=variants, answer=answer)
            questions.append(question)

        attempts.append(MappedAttempt(
            student=student,
            questions=questions,
            completion_date=attempt_completion_date)
        )

    return MappedTestCreate(test=test, attempts=attempts)
