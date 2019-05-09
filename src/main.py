from models.utilities import create_database
from models.parsers import import_oprs_data, import_modiv_data, import_sr1a_data
import models.clustering as my_funcs


def generate_output(municipal_code):
    my_funcs.cluster_scatter_plot(municipal_code)
    my_funcs.dendrogram_plot(municipal_code)
    my_funcs.generate_geojson(municipal_code, '/geojson/data.js')

# Create Database Structure
#create_database()

# Import OPRS Data
#import_oprs_data('/data/1300demo144543(CONT).csv')

# Import MODIV Data
#import_modiv_data('/data/modiv/Monmouth18.txt', 2018)

# Import SR1A Data
#import_sr1a_data('/data/sr1a/2018_SR1A.txt', 2018)

generate_output('39')


print('Files have been created')
