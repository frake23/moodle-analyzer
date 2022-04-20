from pydantic import BaseModel


class MappedTest(BaseModel):
    name: str
    link: str


class MappedStudent(BaseModel):
    first_name = str
    second_name = str
    email = str
    username = str


class MappedGroup(BaseModel):
    name: str


class MappedQuestion(BaseModel):
    text: str
    answer: str
    right_answer: str


class MappedAttempt(BaseModel):
    student: MappedStudent
    group: MappedGroup
    questions: list[MappedQuestion]
    completion_date: str


class MappedTestCreate(BaseModel):
    test: MappedTest
    attempts: list[MappedAttempt]
