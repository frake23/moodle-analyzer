from sqlalchemy import Column, Integer, String

from ..database.engine import Base


class Group(Base):
    __tablename__ = "group"

    group_id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
