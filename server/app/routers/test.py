from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from ..database.engine import get_db
from ..schemas.test import TestCreate, TestItemResponse
from ..mapper import map_test_create
from ..helpers.init_test import init_test
from ..helpers import test_crud

router = APIRouter(
    prefix="/test",
    tags=["test"]
)


@router.post('/')
def create_test(test_create: TestCreate, db: Session = Depends(get_db)):
    mapped_test_create = map_test_create(test_create)
    init_test(db, mapped_test_create)


@router.get('/', response_model=list[TestItemResponse])
def get_tests(db: Session = Depends(get_db)):
    tests = test_crud.get_tests(db)

    return tests if len(tests) != 0 else None
