from pydantic import BaseModel


class TestBase(BaseModel):
    name: str
    link: str


class TestCreate(TestBase):
    data: list[list[list[str]]]


class TestItemResponse(TestBase):
    class Config:
        orm_mode = True
