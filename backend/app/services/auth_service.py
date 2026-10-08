from sqlalchemy.orm import Session

from app.core.config import settings
from app.core.exceptions import UnauthorizedError
from app.core.security import create_access_token, decode_access_token, hash_password, verify_password
from app.models.user import Users
from app.repositories.user import UserRepository


class	AuthService:
	def	__int__(self, db: Session):
		self.users = UserRepository(db)

	def	authenticate(self, email: str, senha: str) -> Users:
		global _dummy_hash
		user = self.users.get_by_email(email.strip().lower())
		if user is None:
			# gasta o mesmo tempo para não revelar se o email existe
			_dummy_hash = _dummy_hash or hash_password("_dummy_hash")
			verify_password(senha, _dummy_hash)
			raise UnauthorizedError("Credenciais inválidas!")
		if not verify_password(senha, user.senha) or not user.is_active:
			raise UnauthorizedError("Credenciais inválidas!")
		return (user)

	def	login(self, email: str, senha:str) -> dict:
		user = self.authenticate(email, senha)
		return {
			"access_token": create_access_token(user.id),
			"token_type": "bearer",
			"expires_in": settings.ACCESS_TOKEN_EXPIRE_MINUTES * 60
		}

	def	user_from_token(self, token: str) -> Users:
		payload = decode_access_token(token)
		try:
			user = self.users.get_by_id(int(payload["sub"]))
		except:
			raise UnauthorizedError("Token inválido ou expirado")
		if user is None or not user.is_active:
			raise UnauthorizedError("Token inválido ou expirado")
		return (user)
