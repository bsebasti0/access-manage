from datetime import datetime


from pydantic import BaseModel, ConfigDict, Field


class	ControllerCreate(BaseModel):
	name: str = Field(
		min_length = 1,
		max_length = 100
	)
	serial_number: str | None = Field(
		default = None,
		max_length = 100
	)


class	ControllerUpdate(BaseModel):
	name: str | None = Field(
		default = None,
		min_length = 1,
		max_length = 100
	)
	serial_number: str | None = Field(
		default = None,
		max_length = 100
	)
	status: str | None = Field(
		default = None,
		max_length = 30
	)
	firmeware_version: str | None = Field(
		default = None,
		max_length = 30
	)


class	ControllerResponse(BaseModel):
	id: int
	name: str
	serial_number: str | None
	status: str
	last_seen: datetime | None
	firmeware_version: str | None

	model_config = ConfigDict(from_attributes=True)
