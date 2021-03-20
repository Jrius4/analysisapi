from sqlalchemy import func, Column,Integer,String, Boolean,DateTime
from sqlalchemy.sql.expression import true
from .database import Base
from datetime import datetime

class Blog(Base):
    __tablename__ = 'blogs'
    id = Column(Integer,primary_key=True,index=True,nullable=False)
    title = Column(String)
    body = Column(String)
    published = Column(Boolean)
    created_at = Column(
           DateTime,
           default=datetime.utcnow(),
            server_default=func.now(),
            nullable=False,
            index=True,
        )
    updated_at = Column(
           DateTime,
           default=datetime.utcnow(),
            server_default=func.now(),
            nullable=False,
            index=True,
        )

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer,primary_key=True,index=True,nullable=False)
    name = Column(String)
    email = Column(String)
    password = Column(String)
    created_at = Column(
           DateTime,
           default=datetime.utcnow(),
            server_default=func.now(),
            nullable=False,
            index=True,
        )
    updated_at = Column(
           DateTime,
           default=datetime.utcnow(),
            server_default=func.now(),
            nullable=False,
            index=True,
        )
