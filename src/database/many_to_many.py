from sqlalchemy import Table, Column, Integer, ForeignKey
from . import Base

course_to_user = Table(
    "course_to_user",
    Base.metadata,
    Column("course_id", Integer, ForeignKey("courses.id")),
    Column("user_id", Integer, ForeignKey("users.id"))
)

user_to_event = Table('user_to_event', Base.metadata,
    Column('user_id', Integer, ForeignKey('users.id')),
    Column('event_id', Integer, ForeignKey('events.id'))
)
