from file_system.model import db, User
from file_system.data_type import UserInfo, Iterable


def init_db() -> None:
    db.create_all()


def reset_db() -> None:
    db.drop_all()
    db.create_all()


def add_user(user_info: UserInfo) -> None:
    db.session.add(User(**user_info))

    db.session.commit()


def add_users(*user_infos: UserInfo) -> None:
    for user_info in user_infos:
        db.session.add(User(**user_info))

    db.session.commit()


def create_default_user() -> None:
    add_users(
        {"username": "admin", "is_admin": True},
        {"username": "user1", "is_admin": False},
        {"username": "user2", "is_admin": False},
        {"username": "user3", "is_admin": False},
        {"username": "user4", "is_admin": False},
        {"username": "user5", "is_admin": False},
    )


def find_all_user() -> Iterable[User]:
    return User.query.all()


def find_user(username: str) -> Iterable[User]:
    return User.query.filter_by(username=username).all()
