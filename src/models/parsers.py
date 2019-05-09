import csv, pandas, math
from sqlalchemy.orm import sessionmaker
from .utilities import get_engine
from .property import Property, property_csv_headers
from .modiv import MODIV, modiv_col_specs
from .sr1a import SR1A, sr1a_col_specs
from datetime import datetime


def import_oprs_data(file_path):
    engine = get_engine()
    Session = sessionmaker(bind=engine)
    session = Session()
    with open(file_path) as csvfile:
        csv_reader = csv.DictReader(csvfile, delimiter=',', quotechar='"')
        for row in csv_reader:
            # list comprehension for row mapping
            values = {key: row[value] for key, value in property_csv_headers.items()}
            # manipulate values for municipal and county code
            values['county_code'] = values['county_code'][0:2]
            values['municipal_code'] = values['municipal_code'][2:4]
            # if empty string found insert null value
            for key, value in values.items():
                if value == '':
                    values[key] = None
            property_obj = Property(**values)
            session.add(property_obj)
            session.commit()
            session.flush()
            print('Added property {}'.format(property_obj.street_addr))


def import_modiv_data(file_path, year):
    engine = get_engine()
    Session = sessionmaker(bind=engine)
    session = Session()
    col_names = [x[0] for x in modiv_col_specs]
    col_specs = [x[1] for x in modiv_col_specs]
    df = pandas.read_fwf(file_path, colspecs=col_specs, names=col_names)
    # Replace the annoying NaN values with None
    df = df.replace({pandas.np.nan: None})
    for row in df.itertuples(index=True, name='modiv'):
        try:
            # Try to find a matching property in the property table
            block = getattr(row, 'block').lstrip('0')
            lot = getattr(row, 'lot').lstrip('0')
            qualifier = getattr(row, 'qualifier')
            county_code = getattr(row, 'county_code')
            municipal_code = getattr(row, 'district_code')

            property_found = session.query(Property)\
                .filter(Property.block == block,
                        Property.lot == lot,
                        Property.qualifier == qualifier,
                        Property.county_code == county_code,
                        Property.municipal_code == municipal_code)\
                .first()

            if property_found is not None:

                insert_values = {}
                insert_values['property_id'] = property_found.id
                insert_values['year'] = year
                insert_values['property_class'] = getattr(row, 'property_class')
                insert_values['building_class_code'] = getattr(row, 'building_class_code')
                insert_values['year_constructed'] = getattr(row, 'year_constructed')
                insert_values['assessment_code'] = getattr(row, 'assessment_code')
                insert_values['acreage'] = getattr(row, 'acreage')
                insert_values['land_value'] = getattr(row, 'land_value')
                insert_values['improvement_value'] = getattr(row, 'improvement_value')
                insert_values['net_value'] = getattr(row, 'net_value')

                modiv_obj = MODIV(**insert_values)
                session.add(modiv_obj)
                session.commit()
                session.flush()
                print('Added CountyCode {} MunicipalCode {} Block {} Lot {} Qualifier {}'
                      .format(county_code, municipal_code, block, lot, qualifier))
            else:
                print('No matching property found for CountyCode {} MunicipalCode {} Block {} Lot {} Qualifier {}'
                      .format(county_code, municipal_code, block, lot, qualifier))
        except Exception as e:
            print(e)
            session.rollback()


def import_sr1a_data(file_path, year):
    engine = get_engine()
    Session = sessionmaker(bind=engine)
    session = Session()
    col_names = [x[0] for x in sr1a_col_specs]
    col_specs = [x[1] for x in sr1a_col_specs]
    df = pandas.read_fwf(file_path, colspecs=col_specs, names=col_names)
    # Replace the annoying NaN values with None
    df = df.replace({pandas.np.nan: None})
    for row in df.itertuples(index=True, name='sr1a'):
        try:
            # Try to find a matching property in the property table
            block = getattr(row, 'block').lstrip('0')
            lot = getattr(row, 'lot').lstrip('0')
            qualifier = getattr(row, 'qualifier')
            county_code = getattr(row, 'county_code')
            municipal_code = getattr(row, 'district_code')
            if county_code != 13:
                print('Not matching county code 13 for CountyCode {} MunicipalCode {} Block {} Lot {} Qualifier {}'
                      .format(county_code, municipal_code, block, lot, qualifier))
                continue

            property_found = session.query(Property) \
                .filter(Property.block == block,
                        Property.lot == lot,
                        Property.qualifier == qualifier,
                        Property.county_code == county_code,
                        Property.municipal_code == municipal_code) \
                .first()

            if property_found is not None:
                insert_values = {}
                insert_values['property_id'] = property_found.id
                insert_values['year'] = year
                insert_values['serial_no'] = getattr(row, 'serial_no')
                insert_values['grantor_name'] = getattr(row, 'grantor_name')
                insert_values['grantor_street'] = getattr(row, 'grantor_street')
                insert_values['grantor_city_state'] = getattr(row, 'grantor_city_state')
                insert_values['grantor_zip'] = getattr(row, 'grantor_zip')
                insert_values['grantee_name'] = getattr(row, 'grantee_name')
                insert_values['grantee_street'] = getattr(row, 'grantee_street')
                insert_values['grantee_city_state'] = getattr(row, 'grantee_city_state')
                insert_values['grantee_zip'] = getattr(row, 'grantee_zip')
                insert_values['deed_book'] = getattr(row, 'deed_book')
                insert_values['deed_page'] = getattr(row, 'deed_page')

                recording_date_str = str(getattr(row, 'recording_date'))
                last_update_date_str = str(getattr(row, 'last_update_date'))

                if len(recording_date_str) is 6:
                    insert_values['recording_date'] = datetime(int('20' + recording_date_str[0:2]),
                                                           int(recording_date_str[2:4]),
                                                           int(recording_date_str[4:6]))
                if len(last_update_date_str) is 6:
                    insert_values['last_update_date'] = datetime(int('20' + last_update_date_str[0:2]),
                                                           int(last_update_date_str[2:4]),
                                                           int(last_update_date_str[4:6]))

                insert_values['reported_sales_price'] = getattr(row, 'reported_sales_price')
                insert_values['verified_sales_price'] = getattr(row, 'verified_sales_price')
                insert_values['assessed_land_value'] = getattr(row, 'assessed_land_value')
                insert_values['assessed_building_value'] = getattr(row, 'assessed_building_value')
                insert_values['assessed_total_value'] = getattr(row, 'assessed_total_value')
                insert_values['sales_ratio'] = getattr(row, 'sales_ratio')
                insert_values['non_usable_sale_type'] = getattr(row, 'non_usable_sale_type')
                insert_values['non_usable_sale_code'] = getattr(row, 'non_usable_sale_code')
                insert_values['year_constructed'] = getattr(row, 'year_constructed')
                insert_values['condo'] = getattr(row, 'condo')
                insert_values['living_space'] = getattr(row, 'living_space')

                sr1a_obj = SR1A(**insert_values)
                session.add(sr1a_obj)
                session.commit()
                session.flush()
                print('Added CountyCode {} MunicipalCode {} Block {} Lot {} Qualifier {}'
                      .format(county_code, municipal_code, block, lot, qualifier))
            else:
                print('No matching property found for CountyCode {} MunicipalCode {} Block {} Lot {} Qualifier {}'
                      .format(county_code, municipal_code, block, lot, qualifier))
        except Exception as e:
            print(e)
            session.rollback()
