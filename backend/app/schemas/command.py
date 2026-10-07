from datetime import datetime

from pydantic import BaseModel, ConfigDict, Field

from app.models.enums import CommandType


class CommandCreate(BaseModel):
	command: CommandType
	value: str | None = Field(
		default = None,
		max_length = 100
	)   # em "release": segundos


class CommandResponse(BaseModel):
	id: int
	device_id: int
	user_id: int | None
	command: str
	value: str | None
	status: str
	created_at: datetime
	expires_at: datetime | None
	sent_at: datetime | None
	acked_at: datetime | None
	response: str | None
	model_config = ConfigDict(from_attributes=True)
