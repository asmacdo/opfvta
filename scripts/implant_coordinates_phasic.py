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
plt.gca().invert_yaxis()
