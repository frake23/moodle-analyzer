from sqlalchemy.orm import Session

from ..models.test import Test


def get_test(db: Session, test_id: int):
    return db.query(Test).filter(Test.test_id == test_id).first()


def get_tests(db: Session):
    return db.query(Test).all()


def create_test(db: Session, test: Test):
    db.add(test)
    db.commit()
    db.refresh(test)

    return test
