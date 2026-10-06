from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

DATA_BASE = "sqlite:///./access_manager.db"

engine = create_engine (
	DATA_BASE,
	connect_args = {"check_same_thread": False}
)

SessionLocal = sessionmaker (
	autoflush= False,
	autocommit= False,
	bind= engine
)

Base = declarative_base()

def	get_db ():
	db = SessionLocal ();

	try:
		yield db
	finally:
		db.close()
