from datetime import datetime

from sqlalchemy import DateTime, Integer, String, Boolean, func
from sqlalchemy.orm import Mapped, mapped_column

from app.core.database import Base
from app.core.utils import utcnow

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
		nullable = False
	)

	senha: Mapped[str] = mapped_column(
		String(100),
		nullable = False
	)

	role: Mapped[str] = mapped_column(
		String(20),
		default = "user",
		server_default = "user",
		nullable = False
	)

	is_active: Mapped[bool] = mapped_column(
		Boolean,
		default = True,
		server_default = "1",
		nullable = False
	)

	Created_at: Mapped[datetime] = mapped_column(
		DateTime,
		default = utcnow,
		server_default = func.now(),
		nullable = False
	)
