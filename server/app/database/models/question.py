from sqlalchemy import Column, Integer, String, Text, Float, ForeignKey

from ..engine import Base


class Question(Base):
    __tablename__ = "question"

    question_id = Column(Integer, primary_key=True)
    text = Column(Text, nullable=False)
    type = Column(String, nullable=False)
    right_answer_number = Column(Float, nullable=True)

    right_answer_variant_id = Column(Integer, ForeignKey(
        'variant.variant_id'), nullable=True)
