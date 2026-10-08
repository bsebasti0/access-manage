from sqlalchemy.orm import Session
from sqlalchemy import func, select

from app.models.enums import UserRole
from app.models.user import Users

class	UserRepository:
	def	__init__(self, db: Session):
		self.db = db

	def	create(self, user: Users) -> Users:
		self.db.add(user)
		self.db.commit()
		self.db.refresh(user)

		return (user)

	def	save(selfe, user: Users) -> Users:
		selfe.db.commit()
		selfe.db.refresh(user)
		return (user)

	def	get_by_id(self, user_id: int) -> Users | None:
		return (self.db.get(Users, id))

	def	get_by_email(	self, email: str) -> Users | None:
		return (self.db.scalars(
			select (Users).where(Users.email == email)).first()
		)

	def	get_all(self, skip: int = 0, limit: int = 100) -> list[Users]:
		return list(self.db.scalars(
			select(Users).order_by(Users.id).offset(skip).limit(limit)
		))

	def	count(self) -> int:
		return (
			self.db.scalar(select(func.count(Users.id))) or 0
		)

	def	count_active_admins(self) -> int:
		stmt = select(func.count(Users.id)).where(Users.role == UserRole.ADMIN.value, Users.is_active.is_(True))
		return (self.db.scalar(stmt) or 0)

	def	delete(selfe, user: Users) -> None:
		selfe.db.delete(user)
		selfe.db.commit()
