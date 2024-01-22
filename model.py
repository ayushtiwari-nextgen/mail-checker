from sqlalchemy import Column,Integer,String 
from pydantic import BaseModel
from sqlalchemy.sql.sqltypes import Type
from sqlalchemy.orm import declarative_base;


Base = declarative_base()


class Insertuser(Base):
    __tablename__ = "usermails"
    nameid:Column(Integer,primary_key = True,nullable=False)
    full_name:Column(String,nullable=False)
    





