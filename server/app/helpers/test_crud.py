from sqlalchemy.orm import Session

from ..database.models.test import Test


def get_test(db: Session, test_id: int):
    return db.query(Test).filter(Test.test_id == test_id).first()


def create_test(db: Session, test: Test):
    db_test = Test(name=test.name, link=test.link)
    db.add(db_test)
    db.commit()
    db.refresh(db_test)

    return db_test
