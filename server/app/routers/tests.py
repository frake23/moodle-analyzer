from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from ..database.engine import get_db
from ..schemas.test_create import TestCreate
from ..utils import map_test_create

router = APIRouter(
    prefix="/tests",
    tags=["tests"]
)

@router.post('/')
def create_test(test_create: TestCreate, db: Session = Depends(get_db)):
    return map_test_create(test_create)
