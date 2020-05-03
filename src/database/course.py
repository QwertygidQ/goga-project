from sqlalchemy import Column, Integer
from sqlalchemy.orm import relationship

from . import Base
from .many_to_many import course_to_user

class Course(Base):
    __tablename__ = "courses"

    id = Column(Integer, nullable=False, primary_key=True)
    users = relationship("User", secondary=course_to_user, back_populates="courses")
