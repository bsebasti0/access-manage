from datetime import datetime

from sqlalchemy import DateTime, Integer, String, ForeignKey, Boolean
from sqlalchemy.orm import Mapped, mapped_column

from app.core.database import Base

class Device(Base):
	__tablename__ = "tb_device"

	id: Mapped[int] = mapped_column(
		Integer,
		primary_key = True,
		index = True
	)

	control_id: Mapped[int] = mapped_column(
		Integer,
		ForeignKey("tb_control.id"),
		nullable = False
	)

	name: Mapped[str] = mapped_column(
		String(100),
		nullable = False
	)

	device_type: Mapped[str] = mapped_column(
		String(100),
		nullable = False
	)

	status: Mapped[bool] = mapped_column(
		Boolean,
		default = False
	)
