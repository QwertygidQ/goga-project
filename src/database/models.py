from . import Base
from .permissions import SaIntFlagType, Perm
from sqlalchemy import Column, Integer, Text, ForeignKey, Table
from sqlalchemy.orm import relationship


class Permission(Base):
    __tablename__ = "permissions"

    user_id = Column(Integer, ForeignKey("users.id"), primary_key=True)
    group_id = Column(Integer, ForeignKey("groups.id"), primary_key=True)

    group = relationship("Group", back_populates="users")
    user = relationship("User", back_populates="groups")

    perm = Column(SaIntFlagType(Perm), default=0)


class Group(Base):
    __tablename__ = "groups"

    id = Column(Integer, primary_key=True)
    title = Column(Text, nullable=False)

    users = relationship("Permission", back_populates="group")


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    tg_id = Column(Integer, nullable=False, unique=True)

    groups = relationship("Permission", back_populates="user")
