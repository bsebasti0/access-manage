from datetime import datetime

from pydantic import BaseModel, Field


class DeviceStateReport(BaseModel):
	channel: int = Field(ge=0, le=255)
	state: str = Field(min_length=1, max_length=30)


class HeartbeatRequest(BaseModel):
	firmware_version: str | None = Field(default=None, max_length=30)
	devices: list[DeviceStateReport] = Field(default_factory=list)


class HeartbeatResponse(BaseModel):
	status: str = "ok"
	server_time: datetime


class PendingCommand(BaseModel):
	type: str = "command"
	id: int
	channel: int
	device_type: str
	command: str
	value: str | None
	expires_at: datetime | None


class CommandAck(BaseModel):
	success: bool = True
	state: str | None = Field(default=None, max_length=30)
	message: str | None = Field(default=None, max_length=255)
