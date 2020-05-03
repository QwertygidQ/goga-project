from sqlalchemy import Column, Integer, Text
from sqlalchemy.orm import relationship

from . import Base

class Course(Base):
    __tablename__ = "courses"

    id = Column(Integer, nullable=False, primary_key=True)
    title = Column(Text, nullable=False)

    users = relationship("User", back_populates="course")
