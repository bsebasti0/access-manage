from enum import StrEnum


class UserRole(StrEnum):
	ADMIN = "admin"
	USER = "user"


class ControllerStatus(StrEnum):
	ONLINE = "Online"
	OFFLINE = "Offline"


class DeviceType(StrEnum):
	LOCK = "lock"   # fechadura
	GATE = "gate"   # cancela


class CommandType(StrEnum):
	LOCK = "lock"
	UNLOCK = "unlock"
	RELEASE = "release"   # destranca N segundos e volta a trancar
	OPEN = "open"
	CLOSE = "close"
	STOP = "stop"
	TOGGLE = "toggle"


class CommandStatus(StrEnum):
	PENDING = "pending"   # criado, ainda não entregue
	SENT = "sent"         # entregue ao controlador
	ACKED = "acked"       # controlador confirmou
	FAILED = "failed"     # controlador reportou falha
	EXPIRED = "expired"   # sem confirmação dentro do TTL


COMMANDS_BY_DEVICE_TYPE = {
	"lock": {"lock", "unlock", "release"},
	"gate": {"open", "close", "stop", "toggle"},
}

# estado do dispositivo depois de um comando bem-sucedido
COMMAND_RESULT_STATE = {
	"lock": "locked", "unlock": "unlocked",
	"open": "open", "close": "closed", "stop": "stopped",
}
