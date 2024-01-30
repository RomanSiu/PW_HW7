from sqlalchemy import Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import declarative_base, Mapped, mapped_column, relationship
import datetime

Base = declarative_base()


class Student(Base):
    __tablename__ = 'students'
    student_id: Mapped[int] = mapped_column(Integer, ForeignKey("student_groups.student_id"), primary_key=True)
    name: Mapped[str] = mapped_column(String(30), nullable=False)
    groups = relationship("StudentGroup", back_populates="students")
    marks = relationship("Mark", back_populates="students")


class StudentGroup(Base):
    __tablename__ = 'student_groups'
    student_id: Mapped[int] = mapped_column(Integer, primary_key=True)
    group_id: Mapped[int] = mapped_column(Integer)
    students = relationship("Student", back_populates="groups")


class Mark(Base):
    __tablename__ = "marks"
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    student_id: Mapped[int] = mapped_column(Integer, ForeignKey("students.student_id"))
    sub_id: Mapped[int] = mapped_column(Integer, ForeignKey("subjects.id"))
    mark: Mapped[int] = mapped_column(Integer)
    got_at: Mapped[datetime.datetime] = mapped_column(DateTime)
    students = relationship("Student", back_populates="marks")
    subjects = relationship("Subject", back_populates="marks")


class Subject(Base):
    __tablename__ = "subjects"
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    sub_name: Mapped[str] = mapped_column(String(20), nullable=False)
    teacher_id: Mapped[int] = mapped_column(Integer, ForeignKey("teachers.id", ondelete="SET NULL",
                                                                onupdate="CASCADE"))
    teachers = relationship("Teacher", back_populates="subjects")
    marks = relationship("Mark", back_populates="subjects")


class Teacher(Base):
    __tablename__ = "teachers"
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String(30), nullable=False)
    subjects = relationship("Subject", back_populates="teachers")