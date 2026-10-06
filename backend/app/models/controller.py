from datetime import datetime

from sqlalchemy import DateTime, Integer, String
from sqlalchemy.orm import Mapped, mapped_column

from app.core.database import Base

class	Controllers(Base):
	__tablename__ = "tb_controllers"

	id: Mapped[int] = mapped_column (
		Integer,
		primary_key = True,
		index = True
	)

	name: Mapped[str] = mapped_column(
		String(100),
		nullable = False
	)

	serial_number: Mapped[str] = mapped_column(
		String(100),
		unique = True,
		nullable = True,
		index = True
	)

	status: Mapped[str] = mapped_column(
		String(30),
		default = "Offline",
		nullable = False
	)

	last_seen: Mapped[datetime | None] = mapped_column(
		DateTime,
		nullable = True
	)

	firmeware_version: Mapped[str | None] = mapped_column(
		String(30),
		nullable = True
	)
