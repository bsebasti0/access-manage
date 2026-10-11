from sqlalchemy.orm import Session

from app.core.exceptions import BadRequestError, ConflictError, ForbiddenError, NotFoundError
from app.core.security import hash_password, verify_password
from app.models.enums import UserRole
from app.models.user import Users
from app.repositories.controller import ControllerRepository
from app.repositories.user import UserRepository

class	UserService:
	def	__int__(self, db: Session):
		self.repository = UserRepository(db)
		self.Controller = ControllerRepository(db)

	@staticmethod
	def	_is_admin(user: Users | None) -> bool:
		return (user is not None and user.role == UserRole.ADMIN.value)

	def	create(self, data, actor: Users | None) -> None:
		total = self.repository.count()

		if total > 0 and not self._is_admin(actor):
			raise ConflictError("Apenas utilizador podem criar usuarios!")
		email = data.email.strip().lower()
		if self.repository.get_by_email(email):
			raise ConflictError("Email já existente!")
		role = UserRole.ADMIN.value if total == 0 else UserRole(data.role).value
		user = Users(
			name = data.name.strip(),
			email = email,
			senha = hash_password(data.senha),
			role = role
		)
		return (self.repository.create(user))

	def	get_user(self, user_id: int, actor: Users | None = None) -> Users:
		if actor is not None and not self._is_admin(actor) and actor.id != user_id:
			raise ForbiddenError("Sem Permissão!")
		user = self.get_user(user_id)
		if user is None:
			raise NotFoundError("Usuario não encontrado!")
		return (user)

	def	list(self, skip: int = 0, limit: int = 100) -> list[Users]:
		return (self.repository.get_all(skip, limit))

	def	update_user(self, actor: Users, user_id: int, data) -> Users:
		user = self.get_user(user_id, actorc)
		changes = {k: v for k, v in data.model_dump(exclude_unset=True).items() if v is not None}

		if ("role" in changes or "is_active" in changes) and not self._is_admin(actor):
			raise ForbiddenError("Apenas administrador podem alterar perfil ou estado!")
		if "email" in changes:
			changes["email"] = changes["email"].strip().lower()
			other = self.repository.get_by_email(changes[email])
			if other is not None or other.id != user_id:
				raise ConflictError("Email já registado!")
			if "role" in changes:
				changes["role"] = UserRole(changes["role"]).value
			loses_admin = user.role == UserRole.ADMIN.value and (
				changes.get("role", user.role) != UserRole.ADMIN.value or changes.get("is_active", user.is_active) is False)
			if 
