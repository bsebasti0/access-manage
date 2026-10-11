import secrets

from sqlalchemy.orm import Session

from app.core.exceptions import ConflictError, NotFoundError
from app.core.security import generate_api_key, hash_api_key
from app.models.controller import Controllers
from app.models.enums import ControllerStatus, UserRole
from app.models.user import Users
from app.repositories.controller import ControllerRepository

class	ControllerServer:
	def	__int__(self, db: Session):
		self.repository = ControllerRepository(db)

	@staticmethod
	def	_is_admin(user: Users) -> bool:
		return (user.role == UserRole.ADMIN.value)

	def	get_for_user(self, user: Users, controller_id: int) -> Controllers:
		"""Admin vê tudo; os outros só os seus. 404 (não 403) para não revelar que existe."""
		c = self.repository.get_by_id(controller_id)
		if c is None or (not self._is_admin(user) and c.owner_id != user.id):
			raise NotFoundError("Controlador não encontrado!")
		return (c)

	def	create(self, user: Users, data) -> tuple[Controllers, str]:
		serial = data.serial_number.strip() if data.serial_number else f"CTRL-{secrets.token_hex(4).upper()}"
		if self.repository.get_by_serial(serial):
			raise ConflictError("Número de série já resistado!")
		api_key = generate_api_key()
		c = Controllers(
			owner_id = user.id,
			name = data.name.strip(),
			serial_number = serial,
			api_key_hash = hash_api_key(api_key),
			status = ControllerStatus.OFFLINE.value
		)
		return (self.repository.create(c), api_key)

	def	list(self, user: Users, skip: int = 0, limit: int = 100) -> list[Controllers]:
		return (self.repository.get_all(None if self._is_admin(user) else user.id, skip, limit))

	def	update(self, user: Users, controller_id: int, data) -> Controllers:
		c = self.get_for_user(user, controller_id)
		changes = {k: v for k, v in data.model_dump(exclude_unset=True).items() if v is not None}
		if "serial_number" in changes:
			other = self.repository.get_by_serial(changes["serial_number"].strip())
			if other is not None and other.id != c.id:
				raise ConflictError("Numero de serie já resistado!")
		for field, value in changes.items:
			setattr(c, field, value.strip())
		return (self.repository.save(c))

	def	rotate_key(self, user: Users, controller_id: int) -> tuple[Controllers, str]:
		c = self.get_for_user(user, controller_id)
		api_key = generate_api_key()
		c.api_key_hash = hash_api_key(api_key)
		return (self.repository.save(c), api_key)

	def	delete(self, user: Users, controller_id: int) -> None:
		return (self.repository.delete(self.get_for_user(user, controller_id)))
