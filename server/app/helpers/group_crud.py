from sqlalchemy.orm import Session

from ..database.models.group import Group


def get_group_by_name(db: Session, name: str):
    return db.query(Group).filter(Group.name == name).first()


def create_group(db: Session, item: list[str]):
    name = item[3]

    if db_group := get_group_by_name(db, name):
        return db_group

    db_group = Group(name=name)
    db.add(db_group)
    db.refresh(db_group)

    return db_group
