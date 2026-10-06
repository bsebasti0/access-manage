from pydantic import BaseModel, Field, EmailStr

class	LoginRequest(BaseModel):
	email: str
	senha: str

class	TokenResponse(BaseModel):
	access_token: str
	token_type: str = "brearer"
