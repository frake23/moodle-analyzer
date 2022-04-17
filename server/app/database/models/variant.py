from sqlalchemy import Column, Integer, Text, ForeignKey

from ..engine import Base


class Variant(Base):
    __tablename__ = "variant"

    variant_id = Column(Integer, primary_key=True)
    text = Column(Text, nullable=False)

    question_id = Column(Integer, ForeignKey(
        'question.question_id'), nullable=False)
