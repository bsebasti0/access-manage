from datetime import datetime
from typing import TYPE_CHECKING

from sqlalchemy import DateTime, Integer, String, ForeignKey, func
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.core.database import Base
from app.core.utils import utcnow

if TYPE_CHECKING:
	from app.models.device import Device

class Commands(Base):
	__tablename__ = "tb_commands"

	id: Mapped[int] = mapped_column(
		Integer,
		primary_key = True,
		index = True
	)

	device_id: Mapped[int] = mapped_column(
		Integer,
		ForeignKey("tb_device.id", ondelete="CASCADE"),
		nullable = False,
		index = True
	)

	user_id: Mapped[int | None] = mapped_column(
		Integer,
		ForeignKey("tb_users.id", ondelete="SET NULL"),
		nullable = False,
		index = True
	)

	command: Mapped[str] = mapped_column(
		String,
		nullable = False
	)

	value: Mapped[str] = mapped_column(
		String,
		nullable = False
	)

	status: Mapped[str] = mapped_column(
		String(20),
		default = "pending",
		server_default = "pending",
		nullable = False,
		index = True
	)

	created_at: Mapped[datetime] = mapped_column(
		DateTime,
		default = utcnow,
		server_default = func.now(),
		nullable = False
	)

	expires_at: Mapped[datetime | None] = mapped_column(
		DateTime,
		nullable = True
	)

	sent_at: Mapped[datetime | None] = mapped_column(
		DateTime,
		nullable = True
	)

	acked_at: Mapped[datetime | None] = mapped_column(
		DateTime,
		nullable = True
	)

	response: Mapped[str | None] = mapped_column(
		String(255),
		nullable = True
	)

	device: Mapped["Device"] = relationship(
		back_populates = "commands"
	)
