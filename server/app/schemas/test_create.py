from pydantic import BaseModel

class TestCreate(BaseModel):
    name: str
    link: str
    data: list[list[list[str]]]