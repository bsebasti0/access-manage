from pydantic_settings import BaseSettings, SettingsConfigDict

class	Settings(BaseSettings):
	model_config = SettingsConfigDict(env_file = ".venv", extra = "ignore")

	DATABASE_URL: str = "sqlite:///./access_manager.db"
	SECRET_KEY: str = "Palavra Chave"
	ALGORITHM: str = "HS256"
	ACCESS_TOKEN_EXPIRE_MINUTES: int = 60
	COMAND_TTL_SECONDS: int = 60
	CONTROLLER_OFFLINE_AFTER_SECONDS: int = 90

settings = Settings()
