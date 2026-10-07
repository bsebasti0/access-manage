from datetime import datetime

from pydantic import BaseModel, ConfigDict, FailFast, Field, EmailStr

from app.models.enum import UserRole


class	UserCreate(BaseModel):
	email: EmailStr

	nome: str = Field(
		min_length = 1,
		max_length = 100
	)

	senha: str = Field(
		min_length = 8,
		max_length = 100
	)

	role: UserRole = UserRole.User

class	UserResponse(BaseModel):
	id: int
	email: EmailStr
	nome: str

	model_config = ConfigDict(from_attributes=True)

class UserUpdate(BaseModel):
	email: EmailStr | None = None
	nome: str | None = Field(
		default=None,
		min_length=1,
		max_length=100
	)
