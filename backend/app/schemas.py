from pydantic import BaseModel
from typing import Optional

class UserCreate(BaseModel):
    username: str
    vpn_key: str
    active: Optional[bool] = True

class UserUpdate(BaseModel):
    username: Optional[str] = None
    vpn_key: Optional[str] = None
    active: Optional[bool] = None

class UserOut(BaseModel):
    id: int
    username: str
    active: bool

    class Config:
        orm_mode = True
