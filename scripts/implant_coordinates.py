import matplotlib.pyplot as plt
import pandas as pd
import matplotlib as mpl
from os import path
from itertools import product
import seaborn as sns

data_path = path.abspath('data/functional_t.csv')
df = pd.read_csv(data_path)

groups_path = path.abspath('data/groups.csv')
groups = pd.read_csv(groups_path)

df = pd.merge(df, groups, on='Subject', how='outer')

df['Task Category'] = df['Task']
task_categories = {
	'CogBr':'Block',
	'CogBm':'Block',
	'CogMwf':'Block',
	'CogB':'Block',
	'JPogP':'Phasic',
	'CogP':'Phasic',
	'JPogT':'Tonic',
	}
df = df.replace({'Task Category': task_categories})
df = df.loc[df['Task Category'] == 'Block']

# Dropna because we do not take into account unimplanted animals
depths = df['Depth rel. skull [mm]'].dropna().unique()
pas = df['PA rel. Bregma [mm]'].dropna().unique()

coordinates = []
for depth, pa in product(depths,pas):
	my_slice = df.loc[(df['PA rel. Bregma [mm]'] == pa) & (df['Depth rel. skull [mm]'] == depth)]
	n = len(my_slice)
	if n != 0:
		coordinates_ = {}
		t = my_slice['Mean VTA t'].mean()
		coordinates_['VTA t '] = t
		coordinates_['Count'] = n
		coordinates_['PA rel. Bregma [mm]'] = pa
		coordinates_['Depth rel. skull [mm]'] = depth
		coordinates.append(coordinates_)
coordinates = pd.DataFrame(coordinates)

cmap = sns.cubehelix_palette(dark=.3, light=.8, as_cmap=True)
ax = sns.scatterplot(
	x="PA rel. Bregma [mm]",
	y="Depth rel. skull [mm]",
	hue='VTA t ',
	size='Count',
	data=coordinates,
	sizes=(15, 150),
	palette=cmap,
	)
plt.gca().invert_yaxis()
