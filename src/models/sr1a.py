from . import Base
from sqlalchemy import Column, Integer, String, ForeignKey, DECIMAL, Date

# Define Fixed Width Column Specs for SR1A file
# See https://www.state.nj.us/treasury/taxation/pdf/lpt/SR1A_FileLayout_Description.pdf
sr1a_col_specs = [
    ['county_code', (0, 2)],
    ['district_code', (2, 4)],
    ['block', (350, 355)],
    ['lot', (359, 364)],
    ['qualifier', (619, 624)],
    ['serial_no', (98, 105)],
    ['grantor_name', (109, 144)],
    ['grantor_street', (144, 169)],
    ['grantor_city_state', (263, 288)],
    ['grantor_zip', (194, 203)],
    ['grantee_name', (203, 238)],
    ['grantee_street', (238, 263)],
    ['grantee_city_state', (263, 288)],
    ['grantee_zip', (288, 297)],
    ['deed_book', (328, 333)],
    ['deed_page', (333, 338)],
    ['recording_date', (344, 350)],
    ['last_update_date', (19, 25)],
    ['reported_sales_price', (37, 46)],
    ['verified_sales_price', (46, 55)],
    ['assessed_land_value', (55, 64)],
    ['assessed_building_value', (64, 73)],
    ['assessed_total_value', (73, 82)],
    ['sales_ratio', (82, 87)],
    ['non_usable_sale_type', (33, 34)],
    ['non_usable_sale_code', (34, 37)],
    ['year_constructed', (652, 656)],
    ['condo', (648, 649)],
    ['living_space', (655, 662)],
]

class SR1A(Base):
    __tablename__ = 'sr1a'

    # Define Database Columns
    id = Column(Integer, primary_key=True)
    property_id = Column(Integer, ForeignKey('property.id'))
    serial_no = Column(String)
    year = Column(Integer)
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

