from sqlalchemy import Column, Integer, ForeignKey

from ..database.engine import Base


class TestQuestion(Base):
    __tablename__ = "test_question"

    test_question_id = Column(Integer, primary_key=True)

    test_id = Column(Integer, ForeignKey('test.test_id'), nullable=False)
    question_id = Column(
        Integer,
        ForeignKey('question.question_id'),
        nullable=False
    )
