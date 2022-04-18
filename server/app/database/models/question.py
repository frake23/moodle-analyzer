from sqlalchemy import Column, Integer, String, Text

from ..engine import Base


class Question(Base):
    __tablename__ = "question"

    question_id = Column(Integer, primary_key=True)
    text = Column(Text, nullable=False)
    type = Column(String, nullable=False)
