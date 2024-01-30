import random
from connect_db import session
from models import Student, StudentGroup, Subject, Mark, Teacher
from faker import Faker
from datetime import datetime


subjects = [(1, "math", 1), (2, "science", 1), (3, "art", 2), (4, "music", 2), (5, "chemistry", 3), (6, "biology", 3),
            (7, "geography", 4), (8, "language", 5)]


def create_name(quantity):
    fake = Faker("uk_UA")
    res = []
    for _ in range(quantity):
        p_name = fake.name()
        name_lst = p_name.split()
        name = f"{name_lst[-1]} {name_lst[0][0].upper()}."
        res.append(name)
    return res


def gen_date():
    start_date = datetime(year=2022, month=1, day=1)
    end_date = datetime(year=2023, month=12, day=31)
    start_stmp = start_date.timestamp()
    end_stmp = end_date.timestamp()
    random_stmp = random.randint(int(start_stmp), int(end_stmp))
    date = datetime.fromtimestamp(random_stmp)
    return date.date()


def gen_students(quantity):
    students_lst = create_name(quantity)
    for i in range(quantity):
        stud = Student(student_id=i+1, name=students_lst[i])
        session.add(stud)


def gen_groups(quantity):
    num = 1
    group_num = 1
    for i in range(quantity):
        group = StudentGroup(student_id=i+1, group_id=group_num)
        session.add(group)
        num += 1
        if num == 18:
            group_num += 1
            num = 1


def gen_teachers(quantity):
    teachers_lst = create_name(quantity)
    for i in range(quantity):
        teacher = Teacher(id=i+1, name=teachers_lst[i])
        session.add(teacher)


def gen_subjects():
    for i in subjects:
        subject = Subject(id=i[0], sub_name=i[1], teacher_id=i[2])
        session.add(subject)


def gen_marks(quantity):
    for i in range(quantity):
        for j in range(20):
            sub = random.randint(1, 8)
            mark = random.randint(2, 5)
            date = gen_date()
            m = Mark(student_id=i+1, sub_id=sub, mark=mark, got_at=date)
            session.add(m)


def main():
    gen_students(50)
    gen_groups(50)
    gen_teachers(5)
    gen_subjects()
    gen_marks(50)


if __name__ == '__main__':
    main()
    session.commit()
