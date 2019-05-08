from . import Base
from sqlalchemy import Column, Integer, String, DECIMAL


# Map CSV Headers to DB Columns from oprs.co.monmouth.nj.us
# Key being database column, value being header
property_csv_headers = {
    'latitude': 'Latitude',
    'longitude': 'Longitude',
    'block': 'Block',
    'lot': 'Lot',
    'qualifier': 'Qual',
    'municipal_code': 'Municipality',
    'county_code': 'Municipality',
    'street_addr': 'Property Location',
}


class Property(Base):
    __tablename__ = 'property'

    id = Column(Integer, primary_key=True)
    latitude = Column(DECIMAL)
    longitude = Column(DECIMAL)
    block = Column(String)
    lot = Column(String)
    qualifier = Column(String)
    municipal_code = Column(Integer)
    county_code = Column(Integer)
    street_addr = Column(String)
