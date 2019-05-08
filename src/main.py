from models.utilities import create_database
from models.parsers import import_oprs_data, import_modiv_data

# Create Database Structure
#create_database()

# Import OPRS Data
#import_oprs_data('/data/1300demo144543(CONT).csv')

# Import MODIV Data
import_modiv_data('/data/modiv/Monmouth18.txt', 2018)

print('done')
