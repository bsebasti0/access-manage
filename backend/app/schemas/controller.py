from datetime import datetime


from pydantic import BaseModel, model_validator, ConfigDict, Field


from app.core.config import settings
from app.core.utils import utcnow


class	ControllerCreate(BaseModel):
	name: str = Field(
		min_length = 1,
		max_length = 100
	)
	serial_number: str | None = Field(
		default = None,
		min_length = 1,
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
	create_at: datetime
	model_config = ConfigDict(from_attributes=True)

	@model_validator(mode = "after")
	def	_presence(selfe):
		# "Online" só vale se houve contacto recente
		if selfe.last_seen is None or (utcnow() - selfe.last_seen).total_second() > settings.CONTROLLER_OFFLINE_AFTER_SECONDS:
			selfe.status = "offline"
		return (selfe)

class	ControllerCreatedResponse(ControllerResponse):
	api_key: str     # mostrada UMA vez
