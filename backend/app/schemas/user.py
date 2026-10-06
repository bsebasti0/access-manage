from datetime import datetime

from pydantic import BaseModel, ConfigDict, FailFast, Field, EmailStr


class	UserCreate(BaseModel):
	email: EmailStr = Field(
		min_length = 1,
		max_length = 100
	)
	nome: str = Field(
		min_length = 1,
		max_length = 100
	)

	senha: str = Field(
		min_length = 8,
		max_length = 100
	)

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
