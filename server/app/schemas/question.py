from pydantic import BaseModel
from ..enums import QuestionType

class QuestionBase(BaseModel):
    text: str

class QuestionItemResponse(QuestionBase):
    class Config:
        orm_mode = True


class QuestionResponse(QuestionBase):
    type: str
    stats: dict[str | int, int]

    class Config:
        orm_mode = True

