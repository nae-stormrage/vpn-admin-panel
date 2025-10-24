from pydantic import BaseModel

class VPNUserCreate(BaseModel):
    username: str

class VPNUserOut(BaseModel):
    id: int
    username: str
    public_key: str
    config_file: str

    class Config:
        orm_mode = True
