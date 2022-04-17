from sqlalchemy import Column, Integer, String, ForeignKey

from ..engine import Base


class Student(Base):
    __tablename__ = "student"

    student_id = Column(Integer, primary_key=True)
    first_name = Column(String, nullable=False)
    second_name = Column(String, nullable=False)
    email = Column(String, nullable=False)
    username = Column(String, nullable=False)

    group_id = Column(Integer, ForeignKey('group.group_id'), nullable=False)
