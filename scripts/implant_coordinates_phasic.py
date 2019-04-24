import matplotlib.pyplot as plt
import matplotlib as mpl
import pandas as pd
from os import path
import seaborn as sns

data_path = path.abspath('data/implant_coordinates_phasic.csv')
df = pd.read_csv(data_path)

cmap = sns.cubehelix_palette(dark=.3, light=.8, as_cmap=True)
ax = sns.scatterplot(
	x="PA rel. Bregma [mm]",
	y="Depth rel. skull [mm]",
	hue='VTA t',
	size='Count',
	data=df,
	sizes=(15, 150),
	palette=cmap,
	)
best_coordinates = df.loc[df['Best Cluster']==True]
lines_markersize = mpl.rcParams['lines.markersize']
plt.scatter(
	best_coordinates['PA rel. Bregma [mm]'].tolist(),
	best_coordinates['Depth rel. skull [mm]'].tolist(),
	c='w',
	s=lines_markersize/8.,
	)
legend = plt.legend()
# Hack to circumvent strange decimal numbering
for i in legend.get_texts():
	text = i.get_text()
	if text == 'Count':
		break
	try:
		text = float(text)
	except ValueError:
		continue
	else:
		text = round(text,2)
		i.set_text(str(text))
plt.gca().invert_yaxis()
