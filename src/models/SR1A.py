from . import Base
from sqlalchemy import Column, Integer, String, ForeignKey, DECIMAL, Date


class SR1A(Base):
    __tablename__ = 'sr1a'

    # Define Database Columns
    id = Column(Integer, primary_key=True)
    real_property_id = Column(Integer, ForeignKey('real_property.id'))
    serial_no = Column(String)
    grantor_name = Column(String)
    grantor_street = Column(String)
    grantor_city_state = Column(String)
    grantor_zip = Column(String)
    grantee_name = Column(String)
    grantee_street = Column(String)
    grantee_city_state = Column(String)
    grantee_zip = Column(String)
    deed_book = Column(String)
    deed_page = Column(String)
    deed_date = Column(Date)
    recording_date = Column(Date)
    last_update_date = Column(Date)
    reported_sales_price = Column(DECIMAL)
    verified_sales_price = Column(DECIMAL)
    assessed_land_value = Column(DECIMAL)
    assessed_building_value = Column(DECIMAL)
    assessed_total_value = Column(DECIMAL)
    sales_ratio = Column(DECIMAL)
    non_usable_sale_type = Column(String)
    non_usable_sale_code = Column(String)
    year_constructed = Column(Integer)
    condo = Column(String)
    living_space = Column(DECIMAL)

    # Define Fixed Width Column Specs for SR1A file
    # See https://www.state.nj.us/treasury/taxation/pdf/lpt/SR1A_FileLayout_Description.pdf
    col_specs = [
        ['serial_no', (99, 105)],
        ['grantor_name', (110, 144)],
        ['grantor_street', (99, 105)],
    ]
