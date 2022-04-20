from sqlalchemy.orm import Session

from ..database.models.group import Group


def get_group_by_name(db: Session, name: str):
    return db.query(Group).filter(Group.name == name).first()


def create_group(db: Session, group: Group):
    if db_group := get_group_by_name(db, group.name):
        return db_group

    db.add(group)
    db.refresh(group)

    return group
