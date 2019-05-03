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
        ['county_code', (1, 2)],
        ['district_code', (3, 4)],
        ['block', (351, 355)],
        ['lot', (360, 364)],
        ['qualifier', (620, 624)],
        ['serial_no', (99, 105)],
        ['grantor_name', (110, 144)],
        ['grantor_street', (99, 105)],
        ['grantor_city_state', (264, 288)],
        ['grantor_zip', (195, 203)],
        ['grantee_name', (204, 238)],
        ['grantee_street', (239, 263)],
        ['grantee_city_state', (264, 288)],
        ['grantee_zip', (289, 297)],
        ['deed_book', (329, 333)],
        ['deed_page', (334, 338)],
        ['recording_date', (345, 350)],
        ['last_update_date', (20, 25)],
        ['reported_sales_price', (38, 46)],
        ['verified_sales_price', (47, 55)],
        ['assessed_land_value', (56, 64)],
        ['assessed_building_value', (65, 73)],
        ['assessed_total_value', (74, 82)],
        ['sales_ratio', (83, 87)],
        ['non_usable_sale_type', (34, 34)],
        ['non_usable_sale_code', (35, 37)],
        ['year_constructed', (652, 655)],
        ['condo', (649, 649)],
        ['living_space', (656, 662)],
    ]
