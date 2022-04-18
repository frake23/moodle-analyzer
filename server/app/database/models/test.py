from sqlalchemy import Column, Integer, String

from ..engine import Base


class Test(Base):
    __tablename__ = "test"

    test_id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    link = Column(String, nullable=False)
