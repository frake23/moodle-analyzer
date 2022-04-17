from sqlalchemy import Column, Integer, ForeignKey, Date

from ..engine import Base


class Attempt(Base):
    __tablename__ = "attempt"

    attempt_id = Column(Integer, primary_key=True)
    completion_date = Column(Date, nullable=False)

    test_id = Column(Integer, ForeignKey('test.test_id'), nullable=False)
    student_id = Column(Integer, ForeignKey(
        'student.student_id'), nullable=False)
