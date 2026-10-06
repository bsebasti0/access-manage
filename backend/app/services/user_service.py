from sqlalchemy.orm import Session

from app.models.user import Users
from app.schemas.user import UserCreate
from app.repositories.user import UserRepository

class	UserService:
	def	__init__(self, db: Session):
		self.repository = UserRepository

	def	create_user(self, data: UserCreate) -> Users:
		existing_user = self.repository.get_by_email(data.email)

		if (existing_user):
			raise ValueError("Email Já registrado!\n")

		user = Users(
			name = data.name,
			email = data.email,
			senha = data.senha
		)

		return (self.repository.create(user))

	def	get_user(self, user_id: int) -> Users | None:
		return (self.repository.get_by_id(user_id))
