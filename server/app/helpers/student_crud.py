from sqlalchemy.orm import Session

from ..database.models.student import Student


def get_student_by_username(db: Session, username: str):
    return db.query(Student).filter(Student.username == username).first()


def create_student(db: Session, item: list[str], group_id: int):
    second_name = item[0]
    first_name = item[1]
    email = item[6]
    username = item[7]

    if db_student := get_student_by_username(db, username):
        return db_student

    db_student = Student(first_name=first_name, second_name=second_name,
                         email=email, username=username, group_id=group_id)
    db.add(db_student)
    db.refresh(db_student)

    return db_student
