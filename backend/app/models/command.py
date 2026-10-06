from datetime import datetime

from sqlalchemy import DateTime, Integer, String, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column

from app.core.database import Base

class Commands(Base):
	__tablename__ = "tb_commands"

	id: Mapped[int] = mapped_column(
		Integer,
		primary_key = True,
		index = True
	)

	device_id: Mapped[int] = mapped_column(
		Integer,
		ForeignKey("tb_device.id"),
		nullable = False
	)

	command: Mapped[str] = mapped_column(
		String,
		nullable = False
	)

	value: Mapped[str] = mapped_column(
		String,
		nullable = False
	)

	created_at: Mapped[DateTime] = mapped_column(
		DateTime,
		default = datetime.utcnow
	)
	
