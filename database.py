from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine, async_sessionmaker
from sqlalchemy.orm import DeclarativeBase

#where to connect, . current directory, blog.db is the file name
#this file gets created automatically
# aiosqlite is the async driver for sqlite
SQLALCHEMY_DATABASE_URL = "sqlite+aiosqlite:///./blog.db"


engine = create_async_engine(
    SQLALCHEMY_DATABASE_URL,
    connect_args={"check_same_thread": False}
)

#this is a factory that creates databse sessions
#session is a transaction with the database
#each session gets its own session
AsyncSessionLocal = async_sessionmaker(
    engine,
    class_=AsyncSession,
    expire_on_commit=False
)

class Base(DeclarativeBase):
    pass

#this is a dependency func that provides sessions to our routes
async def get_db():
    async with AsyncSessionLocal() as session:
        yield session


