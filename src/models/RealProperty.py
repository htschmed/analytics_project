from . import Base
from sqlalchemy import Column, Integer, String, DECIMAL

class RealProperty(Base):
    __tablename__ = 'real_properties'

    id = Column(Integer, primary_key=True)
    latitude = Column(DECIMAL)
    longitude = Column(DECIMAL)
    block = Column(DECIMAL)
    lot = Column(DECIMAL)
    qualifier = Column(DECIMAL)
    owner = Column(String)