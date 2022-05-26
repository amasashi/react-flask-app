from sqlalchemy import Column, Integer, String, DateTime, TIMESTAMP

from cheer.models.database import Base


class User(Base):
    __tablename__ = "m_user"
    user_id = Column(Integer, primary_key=True, nullable=False)
    nickname = Column(String(20))
    password = Column(String(10))
    first_name = Column(String(20))
    first_name_kana = Column(String(20))
    end_name = Column(String(20))
    end_name_kana = Column(String(20))
    mail_address = Column(String(100))
    tel_no = Column(String(12))
    birthday = Column(TIMESTAMP)
    sex = Column(String(1))
    address = Column(String(100))
    url = Column(String(100))
    insert_dt = Column(TIMESTAMP)
    insert_pgm_id = Column(String(10))
    update_dt = Column(TIMESTAMP)
    update_id = Column(String(10))

