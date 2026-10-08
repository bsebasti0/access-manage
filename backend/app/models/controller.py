from datetime import datetime
from typing import TYPE_CHECKING


from sqlalchemy import DateTime, Integer, String, func
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.core.database import Base
from app.core.utils import utcnow

if TYPE_CHECKING:
	from app.models.device import Device

class	Controllers(Base):
	__tablename__ = "tb_controllers"

	id: Mapped[int] = mapped_column (
		Integer,
		primary_key = True,
		index = True
	)

	owner_id: Mapped[int] = mapped_column(
		Integer,
		ForeignKey("tb_users.id", ondelete="RESTRICT"),
		nullable=False,
		index=True
	)

	name: Mapped[str] = mapped_column(
		String(100),
		nullable = False
	)

	api_key_hash: Mapped[str] = mapped_column(
		String(64),
		nullable = True
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

	created_at: Mapped[datetime] = mapped_column(
		DateTime,
		default = utcnow,
		server_default = func.now(),
		nullable = False
	)

	device: Mapped[list["Device"]] = relationship(
		back_populates = "controller",
		cascade = "all, delete-orphan",
		passive_deletes = True
	)
