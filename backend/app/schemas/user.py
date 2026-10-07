from datetime import datetime

from pydantic import BaseModel, ConfigDict, FailFast, Field, EmailStr

from app.models.enums import UserRole


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

	role: UserRole = UserRole.USER

class	UserResponse(BaseModel):
	id: int
	email: EmailStr
	nome: str
	role: UserRole
	is_active: bool
	created_at: datetime
	model_config = ConfigDict(from_attributes=True)

class	UserUpdate(BaseModel):
	email: EmailStr | None = None
	nome: str | None = Field(
		default=None,
		min_length=1,
		max_length=100
	)

	role: UserRole | None = None
	is_active: bool | None = None

class	PasswordChange(BaseModel):
	current_password: str
	new_password: str = Field(
		min_length = 8,
		max_length = 100
	)
