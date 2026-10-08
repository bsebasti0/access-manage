import base64, hashlib, hmac, os
import bcrypt
from datetime import timedelta

import jwt

from app.core.config import settings
from app.core.exceptions import UnauthorizedError
from app.core.utils import utcnow


def	_b64e(raw: bytes) -> str:
	return base64.urlsafe_b64encode(raw).rstrip(b"=").decode()


def	_b64d(text: str) -> bytes:
	return base64.urlsafe_b64decode(text + "=" * (-len(text) % 4))


# ---- senhas: scrypt (biblioteca padrão), formato  scrypt$log2N$r$p$salt$hash
def	hash_password(password: str) -> str:
	salt = bcrypt.gensalt()
	hashed = bcrypt.hashpw(
		password.encode("utf-8"),
		salt
	)
	return (hashed.decode("utf-8"))


def	verify_password(password: str, stored_hash: str | None) -> bool:
	return (
		password.encode("utf-8"),
		stored_hash.encode("utf-8")
	)


# ---- JWT (o "sub" TEM de ser string)
def	create_access_token(user_id: int) -> str:
	now = utcnow()
	payload = {"sub": str(user_id), "iat": now,
			"exp": now + timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES)}
	return jwt.encode(payload, settings.SECRET_KEY, algorithm=settings.ALGORITHM)


def	decode_access_token(token: str) -> dict:
	try:
		return jwt.decode(token, settings.SECRET_KEY, algorithms=[settings.ALGORITHM])
	except jwt.PyJWTError:
		raise UnauthorizedError("Token inválido ou expirado")


# ---- chave dos controladores (alta entropia, por isso sha256 chega)
def	generate_api_key() -> str:
	return _b64e(os.urandom(32))


def	hash_api_key(key: str) -> str:
	return hashlib.sha256(key.encode()).hexdigest()


def	verify_api_key(key: str, stored_hash: str | None) -> bool:
	return bool(stored_hash) and hmac.compare_digest(hash_api_key(key), stored_hash)
