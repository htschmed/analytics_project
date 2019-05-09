import sklearn
from sklearn.cluster import AgglomerativeClustering
import sklearn.metrics as sm
import urllib.parse
import json

import pandas as pd
import matplotlib
import matplotlib.pyplot as plt
import numpy as np

import scipy
from scipy.cluster.hierarchy import dendrogram, linkage
from scipy.cluster.hierarchy import fcluster
from scipy.cluster.hierarchy import cophenet
from scipy.spatial.distance import pdist

from .utilities import get_engine, get_random_color

def get_dataframe(municipal_code):
    engine = get_engine()
    sql = """select
           property.municipal_code,
           property.latitude,
           property.longitude,
           modiv.property_class,
           modiv.building_class_code,
           modiv.year_constructed,
           modiv.assessment_code,
           modiv.acreage,
           modiv.land_value,
           modiv.improvement_value,
           modiv.net_value
           from property
               inner join modiv on property.id = modiv.property_id 
            where modiv.year_constructed is not null and 
                    modiv.acreage is not null and
                    modiv.land_value is not null and
                    modiv.improvement_value is not null and
                    modiv.net_value is not null
                    and property.municipal_code = {}
            """.format(municipal_code)
    df = pd.read_sql(sql, engine)
    return df


def get_accuracy_score(municipal_code):
    df = get_dataframe(municipal_code);
    X = df.ix[:, (1, 2, 5, 7, 8, 9)].values
    y = df.ix[:, (10)].values

    k=4
    Hclustering = AgglomerativeClustering(n_clusters=k, affinity='euclidean', linkage='ward')
    Hclustering.fit_predict(X)
    print(sm.accuracy_score(y, Hclustering.labels_))


def cluster_scatter_plot(municipal_code):
    df = get_dataframe(municipal_code);
    X = df.ix[:, (1, 2, 5, 7, 8, 9)].values
    y = df.ix[:, (10)].values

    k = 6
    Hclustering = AgglomerativeClustering(n_clusters=k, affinity='euclidean', linkage='ward')
    Hclustering.fit_predict(X)
    plt.scatter(X[:,2],X[:,5], c=Hclustering.labels_, cmap='rainbow')
    plt.savefig('/plots/scatter_plot.png')


def generate_geojson(municipal_code, filepath):
    df = get_dataframe(municipal_code);
    X = df.ix[:, (1, 2, 5, 7, 8, 9)].values

    k=12
    Hclustering = AgglomerativeClustering(n_clusters=k, affinity='euclidean', linkage='ward')
    Hclustering.fit_predict(X)
    labels = [x for x in Hclustering.labels_]
    clusters = {}
    for i in range(k):
        clusters[i] = {'color': get_random_color() }
        clusters[i]['features'] = []


    for row in X:
        cluster_label = labels.pop(0)
        feature = {
            'type': 'Feature',
            'properties': {
                'show_on_map': True
            },
            'geometry': {
                'type': 'Point',
                'coordinates': [
                        row[1],
                        row[0]
                    ]
                }
            }
        clusters[cluster_label]['features'].append(feature)

    with open(filepath, 'w') as geo_json_file:
        geo_json_file.write('var clusters=')
        geo_json_file.write(json.dumps(clusters))



def dendrogram_plot(municipal_code):
    df = get_dataframe(municipal_code);
    X = df.ix[:, (1, 2, 5, 7, 8, 9)].values

    Z = linkage(X, 'ward')
    dendrogram(Z, truncate_mode='lastp', p=12, leaf_rotation=45., leaf_font_size=10., show_contracted=True)
    plt.title('Truncated Hierarchical Clustering Dendrogram')
    plt.xlabel('Cluster Size')
    plt.ylabel('Distance')

    plt.axhline(y=6000000)
    plt.axhline(y=3500000)
    plt.savefig('/plots/dendrogram.png')


def test_plt():
    # Data for plotting
    t = np.arange(0.0, 2.0, 0.01)
    s = 1 + np.sin(2 * np.pi * t)

    fig, ax = plt.subplots()
    ax.plot(t, s)

    ax.set(xlabel='time (s)', ylabel='voltage (mV)',
           title='About as simple as it gets, folks')
    ax.grid()

    fig.savefig("/plots/test.png")
