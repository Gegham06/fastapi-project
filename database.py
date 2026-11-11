from sqlalchemy import create_engine
from sqlalchemy.orm import DeclarativeBase, sessionmaker

#where to connect, . current directory, blog.db is the file name
#this file gets created automatically
SQLALCHEMY_DATABASE_URL = "sqlite:///./blog.db"


engine = create_engine(
    SQLALCHEMY_DATABASE_URL,
    connect_args={"check_same_thread": False}
)

#this is a factory that creates databse sessions
#session is a transaction with the database
#each session gets its own session
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

class Base(DeclarativeBase):
    pass

#this is a dependency func that provides sessions to our routes
def get_db():
    with SessionLocal() as db:
        yield db


