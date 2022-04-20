from sqlalchemy.orm import Session

from ..database.models.student import Student


def get_student_by_username(db: Session, username: str):
    return db.query(Student).filter(Student.username == username).first()


def create_student(db: Session, student: Student):
    if db_student := get_student_by_username(db, student.username):
        return db_student

    db.add(student)
    db.refresh(student)

    return student
