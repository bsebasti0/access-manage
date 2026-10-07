from datetime import datetime
from typing import TYPE_CHECKING

from sqlalchemy import DateTime, Integer, String, ForeignKey, Boolean, func, UniqueConstraint
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.core.database import Base
from app.core.utils import utcnow

if TYPE_CHECKING:
	from app.models.command import Commands
	from app.models.controller import Controllers

class	Device(Base):
	__tablename__ = "tb_device"
	__table_args__ = (UniqueConstraint("controller_id", "channel", name = "uq_device_controller_channel"),)

	id: Mapped[int] = mapped_column(
		Integer,
		primary_key = True,
		index = True
	)

	controller_id: Mapped[int] = mapped_column(
		Integer,
		ForeignKey("tb_controllers.id", ondelete = "CASCADE"),
		nullable = False,
		index = True
	)

	name: Mapped[str] = mapped_column(
		String(100),
		nullable = False
	)

	device_type: Mapped[str] = mapped_column(
		String(100),
		nullable = False
	)

	channel: Mapped[int] = mapped_column(
		Integer,
		nullable = False
	)

	state: Mapped[str] = mapped_column(
		String(30),
		default="unknown",
		server_default="unknown",
		nullable = False
	)

	is_active: Mapped[bool] = mapped_column(
		Boolean,
		default = False,
		server_default = "1"
	)

	created_at: Mapped[datetime] = mapped_column(
		DateTime,
		default=utcnow,
		server_default=func.now(),
		nullable=False
	)

	controller: Mapped["Controllers"] = relationship(back_populates="devices")
	commands: Mapped[list["Commands"]] = relationship(
		back_populates="device",
		cascade="all, delete-orphan",
		passive_deletes=True
	)
