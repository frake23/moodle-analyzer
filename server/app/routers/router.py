from fastapi import APIRouter

from .test import router as test_router
from .question import router as question_router

router = APIRouter()

router.include_router(test_router)
router.include_router(question_router)
