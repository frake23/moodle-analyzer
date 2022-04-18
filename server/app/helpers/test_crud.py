from sqlalchemy.orm import Session

from ..database.models.test import Test
from ..schemas.test_create import TestCreate


def get_test(db: Session, test_id: int):
    return db.query(Test).filter(Test.test_id == test_id).first()


def create_test(db: Session, test: TestCreate):
    db_test = Test(name=test.name, link=test.link)
    db.add(db_test)
    db.commit()
    db.refresh(db_test)

    return db_test
