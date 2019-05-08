import csv, pandas
from sqlalchemy.orm import sessionmaker
from .utilities import get_engine
from .property import Property, property_csv_headers
from .modiv import MODIV, modiv_col_specs


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
    top = df.head(10)
    print(top)

def import_sr1a_data():
    pass