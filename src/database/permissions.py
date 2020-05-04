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
    create_subgroups = 2
    invite_admins = 4
    invite_posters = 8
    invite_students = 16
