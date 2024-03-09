import threading

from sqlalchemy import TEXT, Column, Numeric, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import scoped_session, sessionmaker

from config import DB_URI

def start() -> scoped_session:
        engine = create_engine(DB_URL, client_encoding="utf8")
        BASE.metadata.bind = engine
        BASE.metadata.create_all(engine)
        return scoped_session(sessionmaker(bind=engine, autoflush=False))
    BASE = declarative_base()
    SESSION = start()

    INSERTION_LOCK = threading.RLock()

    class Broadcast(BASE):
        __tablename__ = "broadcast"
        id = Column(Numeric, primary_key=True)
        user_name = Column(TEXT)

        def __init__(self, id, user_name):
            self.id = id
            self.user_name = user_name

    Broadcast.__table__.create(checkfirst=True)


# Database MongoDB dan SQL
def add_user(id, user_name):
        with INSERTION_LOCK:
            msg = SESSION.query(Broadcast).get(id)
            if not msg:
                usr = Broadcast(id, user_name)
                SESSION.add(usr)
                SESSION.commit()

def full_userbase():
        users = SESSION.query(Broadcast).all()
        SESSION.close()
        return [int(user.id) for user in users]

def del_user(user_id: int):
        with INSERTION_LOCK:
            user_to_delete = SESSION.query(Broadcast).filter_by(id=user_id).first()
            if user_to_delete:
                SESSION.delete(user_to_delete)
                SESSION.commit()
