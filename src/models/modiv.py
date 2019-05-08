from . import Base
from sqlalchemy import Column, Integer, String, ForeignKey, DECIMAL

# Define Fixed Width Column Specs for SR1A file
# See https://www.state.nj.us/treasury/taxation/lpt/MODIV-Counties/2018/MODIVLayout2018.pdf
modiv_col_specs = [
    ['county_code', (0, 2)],
    ['district_code', (2, 4)],
    ['block', (4, 13)],
    ['lot', (13, 22)],
    ['qualifier', (22, 33)],
    ['property_class', (55, 58)],
    ['building_class_code', (410, 415)],
    ['year_constructed', (415, 419)],
    ['assessment_code', (419, 420)],
    ['acreage', (118, 127)],
    ['land_value', (420, 429)],
    ['improvement_value', (429, 438)],
    ['net_value', (438, 447)],
]


class MODIV(Base):
    __tablename__ = 'modiv'

    id = Column(Integer, primary_key=True)
    property_id = Column(Integer, ForeignKey('property.id'))
    year = Column(Integer)
    property_class = Column(String)
    building_class_code = Column(String)
    year_constructed = Column(Integer)
    assessment_code = Column(String)
    acreage = Column(DECIMAL)
    land_value = Column(DECIMAL)
    improvement_value = Column(DECIMAL)
    net_value = Column(DECIMAL)
