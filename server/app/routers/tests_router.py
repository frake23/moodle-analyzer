from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from ..database.engine import get_db
from ..schemas.test_create import TestCreate

router = APIRouter(
    prefix="/tests",
    tags=["tests"]
)

@router.post('/')
def create_test(test: TestCreate, db: Session = Depends(get_db)):
    print(test)
