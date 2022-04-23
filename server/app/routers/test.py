from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from ..database.engine import get_db
from ..schemas.test import TestCreate, TestItemResponse
from ..mapper import map_test_create
from .. import helpers
from ..helpers import test_crud

router = APIRouter(
    prefix="/test",
    tags=["test"]
)


@router.post('/')
def create_test(test_create: TestCreate, db: Session = Depends(get_db)):
    return helpers.create_test(db, map_test_create(test_create))


@router.get('/', response_model=list[TestItemResponse])
def get_tests(db: Session = Depends(get_db)):
    return test_crud.get_tests(db)
