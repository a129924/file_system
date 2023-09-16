from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class User(db.Model):
    __tablename__ = "USER"

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True, nullable=False)
    is_admin = db.Column(db.Boolean)

    def __init__(self, username: str, is_admin: bool) -> None:
        self.username = username
        self.is_admin = is_admin

    def __repr__(self):
        return f"username : {self.username} , is_admin : {self.is_admin}"
