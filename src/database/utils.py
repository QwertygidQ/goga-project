from typing import List


def add_to_database(obj_list: List[object], session) -> bool:
    try:
        for obj in obj_list:
            session.add(obj)

        session.commit()
    except DatabaseError:
        session.rollback()
        return False

    return True
