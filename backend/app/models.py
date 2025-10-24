from sqlalchemy import Column, Integer, String
from .database import Base

class VPNUser(Base):
    __tablename__ = "vpn_users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True)
    public_key = Column(String, unique=True)
    private_key = Column(String, unique=True)
    config_file = Column(String, unique=True)
