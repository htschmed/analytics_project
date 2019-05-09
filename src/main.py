from models.utilities import create_database
from models.parsers import import_oprs_data, import_modiv_data, import_sr1a_data
from models.clustering import test_plt, dendrogram_plot

# Create Database Structure
#create_database()

# Import OPRS Data
#import_oprs_data('/data/1300demo144543(CONT).csv')

# Import MODIV Data
#import_modiv_data('/data/modiv/Monmouth18.txt', 2018)

# Import SR1A Data
#import_sr1a_data('/data/sr1a/2018_SR1A.txt', 2018)

dendrogram_plot()
#test_plt()

print('done')
