from datetime import datetime

from pydantic import BaseModel, ConfigDict, Field

from app.models.enums import DeviceType

class	DeviceCreated(BaseModel):
	controller_id: int
	name: str = Field(
		min_length = 1,
		max_length = 1000
	)
	device_type: DeviceType
	channel: int = Field(
		ge = 0,
		le = 255
	)


class	DeviceUpdate(BaseModel):
	name: str | None = Field(
		default = None,
		min_length = 1,
		max_length = 100
	)
	channel: int | None = Field(
		default = None,
		ge = 0,
		le = 255
	)
	is_active: bool | None = None

class DeviceResponse(BaseModel):
	id: int
	controller_id: int
	name: str
	device_type: str
	channel: int
	state: str
	is_active: bool
	created_at: datetime
	model_config = ConfigDict(from_attributes=True)
