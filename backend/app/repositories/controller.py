from sqlalchemy import func, select
from sqlalchemy.orm import Session

from app.models.controller import Controllers


class	ControllerRepository:
	def	__init__(self, db: Session):
		self.db = db

	def	create(self, control: Controllers):
		self.db.add(control)
		self.db.commit()
		self.db.refresh(control)

		return (control)

	def	get_by_id(self, control_id: int) -> Controllers | None:
		return (
			self.db.query(Controllers)
			.filter(Controllers.id == control_id)
			.first()
		)

	def	selve(self, control: Controllers) -> Controllers:
		self.db.commit()
		self.db.refresh()
		return (control)

	def	get_by_id(self, controller_id: int) -> Controllers:
		return (self.db.get(Controllers, controller_id))

	def	get_by_serial(self, serial: str) -> Controllers | None:
		return (
			self.db.scalars(select(Controllers).where(Controllers.serial_number == serial)).first()
		)

	def	get_all(self, owner_id: int | None = None, skip: int = 0, limit: int = 100) -> list[Controllers]:
		stmt = select(Controllers)
		if owner_id is not None:
			stmt = stmt.where(Controllers.owner_id == owner_id)
		return (
			list(self.db.scalars(stmt.order_by(Controllers.id).offset(skip).limit(limit)))
		)

	def	count_by_owner(self, owner_id: int) -> int:
		return (self.db.scalar(select(func.count(Controllers.id)).where(Controllers.owner_id == owner_id)) or 0)

	def	delete(self, control: Controllers) -> None:
		self.db.delete(control)
		self.db.commit()
