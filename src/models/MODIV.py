from . import Base
from sqlalchemy import Column, Integer, String, ForeignKey, DECIMAL


class MODIV(Base):
    __tablename__ = 'modiv'

    id = Column(Integer, primary_key=True)
    real_property_id = Column(Integer, ForeignKey('real_property.id'))
    year = Column(Integer)
    property_class = Column(String)
    building_class_code = Column(String)
    year_constructed = Column(Integer)
    assessment_code = Column(String)
    acreage = Column(DECIMAL)
    land_value = Column(DECIMAL)
    improvement_value = Column(DECIMAL)
    net_value = Column(DECIMAL)

# Define Fixed Width Column Specs for SR1A file
    # See https://www.state.nj.us/treasury/taxation/lpt/MODIV-Counties/2018/MODIVLayout2018.pdf
    col_specs = [
        ['serial_no', (99, 105)],
    ]
