from sqlalchemy.orm import Session

from app.models.user import Users

class	UserRepository:
	def	__init__(self, db: Session):
		self.db = db

	def	create(self, user: Users) -> Users:
		self.db.add(user)
		self.db.commit()
		self.db.refresh(user)

		return (user)

	def	get_by_id(self, user_id: int) -> Users | None:
		return (
			self.db.query(Users)
			.filter(Users.id == user_id)
			.first()
		)

	def	get_by_email(self, email: str) -> Users | None:
		return (
			self.db.query(Users)
			.filter(Users.email == email)
			.first()
		)

	def	get_all(self) -> list[Users]:
		return (self.db.query(Users).all())

	def	delete(selfe, user: Users) -> None:
		selfe.db.delete(user)
		selfe.db.commit()
