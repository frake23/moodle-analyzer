from sqlalchemy.orm import Session

from ..database.models.variant import Variant


def get_variant(db: Session, varaint_id: int):
    return db.query(Variant).filter(Variant.varaint_id == varaint_id).first()


def create_variant(db: Session, variant: Variant):
    db.add(variant)
    db.commit()
    db.refresh(variant)

    return variant
