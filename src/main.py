from models.utilities import create_database
from models.parsers import import_oprs_data, import_modiv_data, import_sr1a_data
import models.clustering as my_funcs

# Create Database Structure
#create_database()

# Import OPRS Data
#import_oprs_data('/data/1300demo144543(CONT).csv')

# Import MODIV Data
#import_modiv_data('/data/modiv/Monmouth18.txt', 2018)

# Import SR1A Data
#import_sr1a_data('/data/sr1a/2018_SR1A.txt', 2018)

my_funcs.get_accuracy_score('4')
my_funcs.cluster_scatter_plot('4')
my_funcs.dendrogram_plot('4')

print('done')
