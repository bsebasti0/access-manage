from sqlalchemy import select
from sqlalchemy.orm import Session

from app.models.controller import Controllers
from app.models.device import Device


class DeviceRepository:
	def	__init__(self, db: Session):
		self.db = db

	def	create(self, d: Device) -> Device:
		self.db.add(d)
		self.db.commit()
		self.db.refresh(d)
		return d

	def	save(self, d: Device) -> Device:
		self.db.commit()
		self.db.refresh(d)
		return (d)
	
	def	get_by_id(self, device_id: int) -> Device | None:
		return (self.db.get(Device, device_id))

	def	get_by_controller_channel(self, controller_id: int, channel: int) -> Device | None:
		stmt = select(Device).where(Device.controller_id == controller_id, Device.channel == channel)
		return (self.db.scalars(stmt).first())

	def	get_all(self, owner_id=None, controller_id=None, device_type=None, skip=0, limit=100) -> list[Device]:
		stmt = select(Device)
		if owner_id is not None:   # só dispositivos de controladores deste dono
			stmt = stmt.join(Controllers, Device.controller_id == Controllers.id).where(Controllers.owner_id == owner_id)
		if controller_id is not None:
			stmt = stmt.where(Device.controller_id == controller_id)
		if device_type is not None:
			stmt = stmt.where(Device.device_type == device_type)
		return (list(self.db.scalars(stmt.order_by(Device.id).offset(skip).limit(limit))))

	def	delete(self, d: Device) -> None:
		self.db.delete(d)
		self.db.commit()
