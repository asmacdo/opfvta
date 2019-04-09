import pandas as pd
from copy import deepcopy
from os import path
from itertools import product
from sklearn.cluster import KMeans

def make_summary(df, task_category=''):
        if task_category:
                df = df.loc[df['Task Category']==task_category]
        coordinates = []
        for depth, pa in product(depths,pas):
                my_slice = df.loc[
                        (df['PA rel. Bregma [mm]'] == pa) &
                        (df['Depth rel. skull [mm]'] == depth) &
                        (df['Mean VTA t'].notnull())
                        ]
                n = len(my_slice)
                if n != 0:
                        coordinates_ = {}
                        t = my_slice['Mean VTA t'].mean()
                        coordinates_['VTA t'] = t
                        coordinates_['Count'] = n
                        coordinates_['PA rel. Bregma [mm]'] = pa
                        coordinates_['Depth rel. skull [mm]'] = depth
                        coordinates.append(coordinates_)
        coordinates = pd.DataFrame(coordinates)
        values = coordinates['VTA t'].values

        kmeans = KMeans(n_clusters=2)
        kmeans.fit(values.reshape(-1,1))

        myfilter = [i==1 for i in kmeans.labels_]
        myfilter_ = [i==0 for i in kmeans.labels_]

        filtered_signal = coordinates[myfilter]['VTA t'].mean()
        filtered_signal_ = coordinates[myfilter_]['VTA t'].mean()

        if filtered_signal > filtered_signal_:
                best = myfilter
        elif filtered_signal < filtered_signal_:
                best = myfilter_
        else:
                raise 'K-means clustering detected clusters with the same mean. Something is clearly malfunctioning!'

        coordinates['Best Cluster'] = ''
        coordinates['Best Cluster'] = best

        coordinates.to_csv('../data/implant_coordinates{}.csv'.format(task_category.lower()))

data_path = path.abspath('../data/functional_t.csv')
df = pd.read_csv(data_path)

groups_path = path.abspath('../data/groups.csv')
groups = pd.read_csv(groups_path)
#groups = groups.loc[groups['Genotype_code']=='datg']

df = pd.merge(df, groups, on='Subject', how='outer')

# Dropna because we do not take into account unimplanted animals
depths = df['Depth rel. skull [mm]'].dropna().unique()
pas = df['PA rel. Bregma [mm]'].dropna().unique()

for i in ['','Block','Phasic']:
        make_summary(df, i)
