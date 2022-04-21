from datetime import datetime
from pydantic import BaseModel

from ..enums import QuestionType


class MappedTest(BaseModel):
    name: str
    link: str


class MappedGroup(BaseModel):
    name: str


class MappedStudent(BaseModel):
    first_name: str
    second_name: str
    email: str
    username: str
    group: MappedGroup


class MappedVariant(BaseModel):
    text: str


class MappedAnswer(BaseModel):
    answer_text: str | None
    answer_number: float | None
    answer_variant: MappedVariant | None


class MappedQuestion(BaseModel):
    text: str
    type: QuestionType
    variants: list[MappedVariant] | None


class MappedAttempt(BaseModel):
    student: MappedStudent
    answers: list[MappedAnswer]
    completion_date: datetime


class MappedTestCreate(BaseModel):
    test: MappedTest
    attempts: list[MappedAttempt]
    questions: list[MappedQuestion]
