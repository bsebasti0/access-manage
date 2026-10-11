from sqlalchemy.orm import Session

from app.core.exceptions import ConflictError, NotFoundError
from app.models.device import Device
from app.models.enums import DeviceType, UserRole
from app.models.user import Users
from app.repositories.device import DeviceRepository
from app.services.controller_service import ControllerService
