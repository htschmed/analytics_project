from . import Base
from sqlalchemy import Column, Integer, String, DECIMAL


class RealProperty(Base):
    __tablename__ = 'real_property'

    id = Column(Integer, primary_key=True)
    latitude = Column(DECIMAL)
    longitude = Column(DECIMAL)
    block = Column(DECIMAL)
    lot = Column(DECIMAL)
    qualifier = Column(DECIMAL)
    municipal_code = Column(Integer)
    county_code = Column(Integer)
    street_addr = Column(String)
    zip_code = Column(String)

    # Map CSV Headers to DB Columns from oprs.co.monmouth.nj.us
    csv_headers = []
