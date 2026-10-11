from datetime import timedelta

from sqlalchemy.orm import Session

from app.core.config import settings
from app.core.exceptions import BadRequestError, NotFoundError
from app.core.utils import utcnow
from app.models.command import Commands
from app.models.enums import COMMANDS_BY_DEVICE_TYPE, CommandStatus, CommandType, UserRole
from app.models.user import Users
from app.repositories.command import CommandRepository
from app.services.device_service import DeviceService
