from datetime import datetime

from sqlalchemy import select, update
from sqlalchemy.orm import Session

from app.models.command import Commands
from app.models.controller import Controllers
from app.models.device import Device
from app.models.enums import CommandStatus


class	CommandRepository:
	def	__init__(self, db: Session):
		self.db = db

	def	create(self, c: Commands) -> Commands:
		self.db.add(c)
		self.db.commit()
		self.db.refresh(c)
		return (c)

	def	save(self, c: Commands) -> Commands:
		self.db.commit()
		self.db.refresh(c)
		return (c)

	def	get_by_id(self, command_id: int) -> Commands | None:
		return (self.db.get(Commands, command_id))

	def	get_all(self, owner_id=None, device_id=None, status=None, skip=0, limit=50) -> list[Commands]:
		stmt = select(Commands)
		if owner_id is not None:
			stmt = (stmt.join(Device, Commands.device_id == Device.id)
						.join(Controllers, Device.controller_id == Controllers.id)
						.where(Controllers.owner_id == owner_id))
		if device_id is not None:
			stmt = stmt.where(Commands.device_id == device_id)
		if status is not None:
			stmt = stmt.where(Commands.status == status)
		return (list(self.db.scalars(stmt.order_by(Commands.id.desc()).offset(skip).limit(limit)))
)
	def	get_pending_for_controller(self, controller_id: int) -> list[Commands]:
		stmt = (select(Commands).join(Device, Commands.device_id == Device.id)
				.where(Device.controller_id == controller_id, Commands.status == CommandStatus.PENDING.value)
				.order_by(Commands.id))
		return (list(self.db.scalars(stmt)))

	def	claim_for_delivery(self, command_id: int, now: datetime) -> bool:
		"""pending -> sent de forma ATÓMICA. Evita entregar o mesmo comando 2x
		e evita que um 'sent' tardio sobrescreva um 'acked'."""
		stmt = (update(Commands)
				.where(Commands.id == command_id, Commands.status == CommandStatus.PENDING.value)
				.values(status=CommandStatus.SENT.value, sent_at=now))
		result = self.db.execute(stmt); self.db.commit()
		return (result.rowcount or 0) == 1

	def	expire_stale(self, now: datetime) -> int:
		stmt = (update(Commands)
				.where(Commands.status.in_([CommandStatus.PENDING.value, CommandStatus.SENT.value]),
					Commands.expires_at.is_not(None), Commands.expires_at < now)
				.values(status=CommandStatus.EXPIRED.value))
		result = self.db.execute(stmt); self.db.commit()
		return (result.rowcount or 0)
