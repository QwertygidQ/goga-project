from enum import IntFlag
import sqlalchemy as sa


class SaIntFlagType(sa.types.TypeDecorator):
    impl = sa.Integer

    def __init__(self, intflagtype, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._intflagtype = intflagtype

    def process_bind_param(self, value, dialect):
        return value.value

    def process_result_value(self, value, dialect):
        return self._intflagtype(value)


class Perm(IntFlag):
    post = 1
    invite_posters = 2
    invite_students = 4

    @staticmethod
    def all():
        return Perm.post | Perm.invite_posters | Perm.invite_students
