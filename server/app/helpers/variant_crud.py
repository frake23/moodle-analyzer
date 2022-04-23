from sqlalchemy.orm import Session

from ..models.variant import Variant


def get_variant(db: Session, question_id: int, text: str):
    return db\
        .query(Variant)\
        .filter(Variant.question_id == question_id)\
        .filter(Variant.text == text)\
        .first()


def create_variant(db: Session, variant: Variant):
    if db_variant := get_variant(db, variant.question_id, variant.text):
        return db_variant

    db.add(variant)
    db.commit()
    db.refresh(variant)

    return variant
