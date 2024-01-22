from fastapi import FastAPI
from pydantic import BaseModel
from sqlalchemy import engine,create_engine
from sqlalchemy.engine import URL
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import session,sessionmaker,Session,scoped_session
from fastapi.responses import JSONResponse
from sqlalchemy import Column,Integer,String 
from pydantic import BaseModel
from sqlalchemy.sql.sqltypes import Type


url = URL.create(
    drivername = "postgresql",
    username = "postgres",
    password ="Ngc12345678",
    host = "localhost",
    database = "postgres",
    port = 5432)


engine =create_engine(url,pool_size=5,max_overflow=10)
sessions = sessionmaker(autocommit = False,autoflush = False,bind = engine)
Session = sessions()

Base = declarative_base()

class Insertuser(Base):
    __tablename__ = "usermails"
    id=Column(Integer,primary_key = True,nullable=False)
    fullname=Column(String,nullable=False)


Base.metadata.create_all(engine)
app = FastAPI()

@app.get("/")
async def get_name():
    session_local = sessions()
    name_query = session_local.query(Insertuser)
    result = name_query.all()
    shortened_names = [check(item.fullname) for item in result]
    lengths = [checklength(item.fullname) for item in result]
    session_local.close()  
    return {"shortened_names": shortened_names,"lenghts": lengths}
    
    
@app.post("/create")
async def insert_name(fullname:str):
    user = Insertuser(fullname = fullname)
    Session.add(user)
    Session.commit()
    return{"useradd":user.fullname}


def check(name):
    name = name.strip()
    checker_name = []
    
    if name:
        i =0
        while(name[i] != '@'):
            checker_name.append(name[i])
            i = i+1
    result = ''.join(checker_name)      
    return result


def checklength(name):
    name_length = len(name)
    return name_length
       








