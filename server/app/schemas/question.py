from pydantic import BaseModel


class QuestionBase(BaseModel):
    text: str


class QuestionItemResponse(QuestionBase):
    question_id: int

    class Config:
        orm_mode = True


class QuestionResponse(QuestionBase):
    type: str
    stats: dict[str | int, int]

    class Config:
        orm_mode = True
