from sqlalchemy import Column, Integer, Table, ForeignKey
from sqlalchemy.orm import relationship
from . import Base

course_to_user = Table(
    "course_to_user",
    Base.metadata,
    Column("course_id", Integer, ForeignKey("course.id")),
    Column("user_id", Integer, ForeignKey("user.id"))
)

class Course(Base):
    __tablename__ = "courses"

    id = Column(Integer, nullable=False, primary_key=True)
    users = relationship("User", secondary=course_to_user)
