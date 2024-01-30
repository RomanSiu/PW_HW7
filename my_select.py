from sqlalchemy import select, func, and_
from connect_db import session
from models import Student, StudentGroup, Subject, Mark, Teacher


def select1():
    q = session.execute(select(Student.name, func.avg(Mark.mark))
                        .join(Mark).group_by(Mark.student_id, Student.name)
                        .order_by(func.avg(Mark.mark).desc()).limit(5)).mappings().all()
    return q


def select2():
    q = session.execute(select(Student.name, Subject.sub_name, func.avg(Mark.mark)).select_from(Mark)
                        .join(Student).join(Subject).where(Mark.sub_id == 1)
                        .group_by(Mark.student_id, Student.name, Subject.sub_name)
                        .order_by(func.avg(Mark.mark).desc()).limit(1)).mappings().all()
    return q


def select3():
    q = session.execute(select(StudentGroup.group_id, Subject.sub_name, func.avg(Mark.mark))
                        .select_from(Mark).join(Student).join(StudentGroup).join(Subject)
                        .where(Mark.sub_id == 1).group_by(StudentGroup.group_id, Subject.sub_name)).mappings().all()
    return q


def select4():
    q = session.execute(select(func.avg(Mark.mark).label("avg mark"))).mappings().all()
    return q


def select5():
    q = session.execute(select(Teacher.name, Subject.sub_name).join(Subject)).mappings().all()
    return q


def select6():
    q = session.execute(select(StudentGroup.group_id.label("group №"), Student.name)
                        .join(Student).where(StudentGroup.group_id == 1)).mappings().all()
    return q


def select7():
    q = session.execute(select(StudentGroup.group_id.label("group №"), Subject.sub_name.label("subject"),
                               Student.name, Mark.mark).select_from(Mark)
                        .join(Student).join(StudentGroup).join(Subject)
                        .where(and_(StudentGroup.group_id == 2, Subject.id == 1))).mappings().all()
    return q


def select8():
    q = session.execute(select(Teacher.name, Subject.sub_name.label("subject"), func.avg(Mark.mark).label("avg mark"))
                        .select_from(Mark).join(Subject).join(Teacher)
                        .group_by(Subject.sub_name, Teacher.name)).mappings().all()
    return q


def select9():
    q = session.execute(select(Student.name, Subject.sub_name.label("subject")).select_from(Mark)
                        .join(Student).join(Subject).where(Mark.student_id == 6)
                        .group_by(Subject.sub_name, Student.name)).mappings().all()
    return q


def select10():
    q = session.execute(select(Student.name, Teacher.name, Subject.sub_name).select_from(Mark)
                        .join(Student).join(Subject).join(Teacher).where(and_(Student.student_id == 1, Teacher.id == 1))
                        .group_by(Subject.sub_name, Student.name, Teacher.name)).mappings().all()
    return q


def select11():
    q = session.execute(select(Student.name.label("student"), Teacher.name.label("teacher"),
                               func.avg(Mark.mark).label("avg mark")).select_from(Mark)
                        .join(Student).join(Subject).join(Teacher)
                        .where(and_(Student.student_id == 1, Teacher.id == 3))
                        .group_by(Subject.sub_name, Student.name, Teacher.name)).mappings().all()
    return q


if __name__ == "__main__":
    res = select11()
    print(res)
