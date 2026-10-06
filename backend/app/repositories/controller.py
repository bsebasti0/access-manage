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

	def get_by_id(self, control_id: int) -> Controllers | None:
		return (
			self.db.query(Controllers)
			.filter(Controllers.id == control_id)
			.first()
		)

	def get_by_user(self, user_id: int) -> list[Controllers]:
		return (
			self.db.query(Controllers)
			.filter(Controllers.user_id == user_id)
			.all()
		)

	def delete(self, control: Controllers) -> None:
		self.db.delete(control)
		self.db.commit()
