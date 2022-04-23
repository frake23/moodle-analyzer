from sqlalchemy import Column, Integer, Text, Float, ForeignKey, String

from ..database.engine import Base


class Answer(Base):
    __tablename__ = "answer"

    answer_id = Column(Integer, primary_key=True)
    answer_text = Column(Text, nullable=True)
    answer_number = Column(Float, nullable=True)
    answer_variant = Column(String, nullable=True)

    attempt_id = Column(
        Integer,
        ForeignKey('attempt.attempt_id'),
        nullable=False
    )
    question_id = Column(
        Integer,
        ForeignKey('question.question_id'), nullable=False
    )
