import matplotlib.pyplot as plt
import matplotlib as mpl
import pandas as pd
from os import path
import seaborn as sns

data_path = path.abspath('data/implant_coordinates.csv')
df = pd.read_csv(data_path)
lines_markersize = mpl.rcParams['lines.markersize']

df = df.rename(columns={
	'VTA t': 'VTA t ',
	'Count': 'n ',
	})

cmap = sns.cubehelix_palette(dark=.3, light=.8, as_cmap=True)
ax = sns.scatterplot(
	x='PA rel. Bregma [mm]',
	y='Depth rel. skull [mm]',
	hue='VTA t ',
	size='n ',
	data=df,
	sizes=(40, 150),
	palette=cmap,
	)
best_coordinates = df.loc[df['PA rel. Bregma [mm]']>=-3.25]
plt.scatter(
	best_coordinates['PA rel. Bregma [mm]'].tolist(),
	best_coordinates['Depth rel. skull [mm]'].tolist(),
	c='w',
	s=lines_markersize/8.,
	)
# Hack to circumvent strange decimal numbering
handles, labels = ax.get_legend_handles_labels()
newlabels = []
for i in labels:
	try:
		i = float(i)
	except:
		pass
	else:
		i = '{0:.1f}'.format(i)
		i = str(i)
	newlabels.append(i)
ax.legend(handles, newlabels)
plt.gca().invert_yaxis()
