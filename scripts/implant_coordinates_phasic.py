import matplotlib.pyplot as plt
import matplotlib as mpl
import pandas as pd
from os import path
import seaborn as sns

data_path = path.abspath('data/implant_coordinates_phasic.csv')
df = pd.read_csv(data_path)
lines_markersize = mpl.rcParams['lines.markersize']

cmap = sns.cubehelix_palette(dark=.3, light=.8, as_cmap=True)
ax = sns.scatterplot(
	x="PA rel. Bregma [mm]",
	y="Depth rel. skull [mm]",
	hue='VTA t',
	size='Count',
	data=df,
	sizes=(15, 150),
	palette=cmap,
	sizes=(3,6),
	)
best_coordinates = df.loc[df['Best Cluster']==True]
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
		i = "{0:.1f}".format(i)
		i = str(i)
	newlabels.append(i)
ax.legend(handles, newlabels)
plt.gca().invert_yaxis()
