from pydantic import BaseModel


class TestBase(BaseModel):
    name: str
    link: str | None


class TestCreate(TestBase):
    data: list[list[list[str]]]


class TestItemResponse(TestBase):
    test_id: int

    class Config:
        orm_mode = True
