from datetime import datetime

from sqlalchemy import DateTime, Integer, String
from sqlalchemy.orm import Mapped, mapped_column

from app.core.database import Base

class	Users(Base):
	__tablename__ = "tb_users"

	id: Mapped[int] = mapped_column(
		Integer,
		primary_key = True,
		index = True
	)

	email: Mapped[str] = mapped_column(
		String(100),
		unique = True,
		index = True
	)

	nome: Mapped[str] = mapped_column(
		String(100),
		nullable = True
	)

	senha: Mapped[str] = mapped_column(
		String(100),
		nullable = True
	)
